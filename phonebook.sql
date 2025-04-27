-- phonebook атты кестені құру
CREATE TABLE IF NOT EXISTS phonebook1 (
    user_id SERIAL PRIMARY KEY,             -- Бірегей ID, автоматты түрде артады
    username VARCHAR(255),                  -- Пайдаланушының аты
    phone_number VARCHAR(20)                -- Телефон нөмірі
);

-- phonebook1 кестесінен барлық деректерді шығару
SELECT * FROM phonebook1
WHERE phone_number LIKE '5%' OR phone_number LIKE '9%';

--SELECT * FROM phonebook1 WHERE phone_number LIKE '9%';
--SELECT * FROM phonebook1 WHERE phone_number LIKE '5%';