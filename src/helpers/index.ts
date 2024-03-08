import mlbTeams from "../assets/mlbTeams.json";

export function getTeamColors(teamId: number): Record<string, string> {
  for (const team of mlbTeams) {
    if ("colors" in team && team["colors"] && teamId == team.id) {
      return team["colors"];
    }
  }

  return {};
}
