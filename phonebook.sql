CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    phone_number TEXT NOT NULL
);

-- 创建插入或更新用户存储过程
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name TEXT,
    p_surname TEXT,
    p_phone_number TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name AND surname = p_surname) THEN
        UPDATE phonebook
        SET phone_number = p_phone_number
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook (name, surname, phone_number)
        VALUES (p_name, p_surname, p_phone_number);
    END IF;
END;
$$;

-- 创建批量插入用户存储过程
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_surnames TEXT[],
    p_phone_numbers TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    phone_valid BOOLEAN;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        phone_valid := p_phone_numbers[i] ~ '^\d{10}$';  -- 10位数字

        IF phone_valid THEN
            INSERT INTO phonebook (name, surname, phone_number)
            VALUES (p_names[i], p_surnames[i], p_phone_numbers[i]);
        ELSE
            RAISE NOTICE 'Invalid phone number: % for user % %', p_phone_numbers[i], p_names[i], p_surnames[i];
        END IF;
    END LOOP;
END;
$$;

-- 创建删除用户存储过程
CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(
    p_username TEXT,
    p_phone_number TEXT
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_username IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_username;
    END IF;

    IF p_phone_number IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone_number = p_phone_number;
    END IF;
END;
$$;


CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT id, name, surname, phone_number
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_phonebook_page(limit INT, offset INT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT id, name, surname, phone_number
    FROM phonebook
    ORDER BY id
    LIMIT limit OFFSET offset;
END;
$$ LANGUAGE plpgsql;
