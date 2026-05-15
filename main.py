import streamlit as st

from src.crew import ExplainCrew
from src.schema import OutputResult
from src.utils import load_css

load_css('./src/style.css')

st.set_page_config(
    page_title='AI Объяснитель Тем',
    page_icon='📚',
    layout='wide'
)

st.title('🤖AI Агент для объяснения тем')
st.markdown('---')

st.subheader('🎓Что хотите изучить?')
topic = st.text_input(
    label='Введите тему:',
    help='Введите любую тему которую хотите понять'
)

col1, col2 = st.columns([1,4])

with col1:
    start_button = st.button('🚀Начать',type='primary',use_container_width=True)

if start_button:
    if not topic:
        st.warning('❌ Пожалуйста, введите тему')
    else:
        with st.spinner('🤖 Агент работает... Это может занять 1-2 минуты'):
            try:
                progress_bar = st.progress(0)
                status_text = st.empty()

                status_text.text('🔍 Исследователь ищет информацию...')
                progress_bar.progress(33)

                input_data = {'topic': topic}

                result = ExplainCrew().crew().kickoff(inputs=input_data)

                status_text.text('📝 Формируем результат...')
                progress_bar.progress(66)

                if hasattr(result, 'pydantic') and result.pydantic:
                    output: OutputResult = result.pydantic

                    status_text.text('✅ Готово!')
                    progress_bar.progress(100)

                    st.success('✅ Объяснение готово!')
                    st.divider()

                    st.header(f'{output.topic_name}')

                    st.subheader('💡 Кратко')
                    st.info(f'{output.description}')

                    st.subheader('📃Основные термины')
                    st.write(', '.join(output.key_consepts))

                    st.subheader('📚 Подробное объяснение')
                    st.markdown(f'{output.detailed_description}')

                    st.subheader('💭 Примеры использования')
                    for i, example in enumerate(output.examples, 1):
                        st.markdown(f'**{i}**. {example}')

                    st.subheader('🎯 Главное запомнить')
                    st.success(f'{output.conclution}')


            except Exception as e:
                st.exception(e)