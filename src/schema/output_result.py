from pydantic import BaseModel, Field

from typing import List

class OutputResult(BaseModel):
    topic_name: str = Field(
        ...,
        description='Название темы',
        examples='Объектно-ориентированное программирование'
    )

    description: str = Field(
        ...,
        description='Краткое объяснение в 3-4 предложениях для быстрого понимания',
        examples='ООП — это подход к программированию, основанный на объектах...'
    )

    key_consepts: List[str] = Field(
        ...,
        description='Список из ключевых терминов',
        examples=['Класс','Объект','Экземпляр','Наследование']
    )

    detailed_description: str = Field(
        ...,
        description='Подробное объяснение сути: как работает, зачем нужно, основные принципы'
    )

    examples: List[str] = Field(
        ...,
        description='Практические примеры использования (минимум 3 примера из реальной жизни)',
        min_items=3
    )

    conclution: str = Field(
        ...,
        description='Итоговый вывод: главное, что нужно запомнить'
    )