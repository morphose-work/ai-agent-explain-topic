from crewai.tools import BaseTool

from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

class WebSearchTool(BaseTool):
    name: str = 'websearch_tool'
    description: str = 'Поиск в интернете. Принимает поисковый запрос.Возвращает релевантные результаты с ссылками.'

    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)
