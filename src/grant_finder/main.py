#!/usr/bin/env python
import os
from typing import Any
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from grant_finder.crews.grant_finding_team.grant_finding_team import GrantFindingTeam

# Define structured data models
class OrgProfile(BaseModel):
    org_discription: str = "",
    selected_sources: str = ""



class GrantFindingFlow(Flow[OrgProfile]):
    """Flow for grant finding process"""

    @start()
    def start_research(self):
        print("Starting grant finding flow...")
        self.state.org_discription="Indira gandhi NGO is a non-profit organization focused on education and healthcare in rural India.Its in need of funding of around 50 thousand Indian Rupees to expand its reach and impact."

    @listen(start_research)
    def research(self):
        print("Searching for funding sources...")
        result = GrantFindingTeam().crew().kickoff(inputs={
                "org_description": self.state.org_discription,
                "selected_sources": self.state.selected_sources
        })
        funding_sources_text = result.raw
        print("Funding sources found:")
        print(funding_sources_text)
        self.state.selected_sources = funding_sources_text
        return funding_sources_text
    @listen(research)
    def save_report(self, funding_sources_text: str):
        print("Saving funding sources to output/funding_sources.md ...")
        os.makedirs("output", exist_ok=True)
        with open("output/funding_sources.md", "w", encoding="utf-8") as f:
            f.write(funding_sources_text)
        print("File saved successfully.")

def kickoff():
    flow = GrantFindingFlow()
    flow.kickoff()
    flow.plot("grant_finding_flow")
    print("Flow visualization saved to grant_finding_flow.html")
    print("\n=== Grant Finding Flow Completed ===")
    print("Check output/final_grant_report.md for the generated report.")

if __name__ == "__main__":
    kickoff()
