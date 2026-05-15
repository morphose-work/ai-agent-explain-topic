from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

from typing import List

from src.tools import WebSearchTool
from src.utils import ENV_READER
from src.schema import OutputResult

@CrewBase
class ExplainCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    env_reader = ENV_READER()

    llm = LLM(
        model=env_reader.OPENROUTER_MODEL,
        api_key=env_reader.get_api_key(),
        base_url=env_reader.OPENROUTER_BASE_URL
    )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[WebSearchTool()],
            llm=self.llm
        )
    
    @agent
    def teacher(self) -> Agent:
        return Agent(
            config=self.agents_config['teacher'],
            llm=self.llm
        )
    
    @task
    def researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['researcher_task']
        )
    
    @task
    def teacher_task(self) -> Task:
        return Task(
            config=self.tasks_config['teacher_task'],
            output_pydantic=OutputResult
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )