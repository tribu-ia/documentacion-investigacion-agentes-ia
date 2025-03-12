from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from sw_crew.tools.TrelloTool import trello_tool_create
from sw_crew.tools.TrelloTool import trello_tool_comment
from sw_crew.tools.TrelloTool import trello_tool_list
from sw_crew.tools.TrelloTool import trello_tool_change_column

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class SwCrew():
	"""SwCrew crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	trello_tool_create = trello_tool_create
	trello_tool_comment = trello_tool_comment
	trello_tool_list = trello_tool_list
	trello_tool_change_column = trello_tool_change_column


    # If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def product_owner_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['product_owner_agent'],
			verbose=True,
			tools=[self.trello_tool_create, self.trello_tool_comment, self.trello_tool_change_column],
			llm="gpt-4o",

		)

	@agent
	def qa_engineer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['qa_engineer_agent'],
			verbose=True,
			tools=[self.trello_tool_list, self.trello_tool_comment],
			llm='gpt-4o'
		)

	@agent
	def senior_engineer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_engineer_agent'],
			verbose=True,
			tools=[self.trello_tool_list, self.trello_tool_comment, self.trello_tool_change_column],
			llm='gpt-4o'
		)


	# To learn more about structured task outputs,
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def user_story_task(self) -> Task:
		return Task(
			config=self.tasks_config['user_story_task'],
			output_file='po_user_story.md'
		)

	@task
	def testing_scenarios_task(self) -> Task:
		return Task(
			config=self.tasks_config['testing_scenarios_task'],
			output_file='qa_testing_scenarios.md'
		)

	@task
	def tech_feasibility_task(self) -> Task:
		return Task(
			config=self.tasks_config['tech_feasibility_task'],
			output_file='dev_tech_feasibility.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ThreeAmigos crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)