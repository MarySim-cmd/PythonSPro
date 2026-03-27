from sqlalchemy import text

def test_insert(db_connection):
    """Добавление предмета с id=16 - японский язык"""
    # Удаляем, если есть
    db_connection.execute(text("DELETE FROM subject WHERE subject_id = 16"))
    
    # Добавляем предмет
    db_connection.execute(text("INSERT INTO subject(subject_id, subject_title) VALUES (16, 'японский язык')"))
    
    # ПРОВЕРКА
    result = db_connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = 16")
    ).fetchone()
    
    assert result is not None, "Предмет не был добавлен"
    assert result[0] == "японский язык", f"Ожидалось 'японский язык', получено '{result[0]}'"


def test_update(db_connection):
    """Изменение предмета с id=16 с 'японский язык' на 'китайский язык'"""
    # Если записи нет - создаем
    count = db_connection.execute(text("SELECT COUNT(*) FROM subject WHERE subject_id = 16")).scalar()
    if count == 0:
        db_connection.execute(text("INSERT INTO subject(subject_id, subject_title) VALUES (16, 'японский язык')"))
    
    # Изменяем название
    db_connection.execute(text("UPDATE subject SET subject_title = 'китайский язык' WHERE subject_id = 16"))
    
    # ПРОВЕРКА
    result = db_connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = 16")
    ).fetchone()
    
    assert result is not None, "Предмет не найден после обновления"
    assert result[0] == "китайский язык", f"Ожидалось 'китайский язык', получено '{result[0]}'"


def test_delete(db_connection):
    """Удаление предмета с id=16"""
    # Если записи нет - создаем
    count = db_connection.execute(text("SELECT COUNT(*) FROM subject WHERE subject_id = 16")).scalar()
    if count == 0:
        db_connection.execute(text("INSERT INTO subject(subject_id, subject_title) VALUES (16, 'японский язык')"))
    
    # Удаляем предмет
    db_connection.execute(text("DELETE FROM subject WHERE subject_id = 16"))
    
    # ПРОВЕРКА
    result = db_connection.execute(
        text("SELECT COUNT(*) FROM subject WHERE subject_id = 16")
    ).scalar()
    
    assert result == 0, f"Предмет не был удален, найдено {result} записей с id=16"