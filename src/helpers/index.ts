import mlbTeams from "../assets/mlbTeams.json";

import AthleticsLogo from "../assets/logos/oakland-athletics-logo.svg";
import PiratesLogo from "../assets/logos/pittsburgh-pirates-logo.svg";
import PadresLogo from "../assets/logos/san-diego-padres-logo.svg";
import MarinersLogo from "../assets/logos/seattle-mariners-logo.svg";
import GiantsLogo from "../assets/logos/san-francisco-giants-logo.svg";
import CardinalsLogo from "../assets/logos/st.-louis-cardinals-logo.svg";
import RaysLogo from "../assets/logos/tampa-bay-rays-logo.svg";
import RangersLogo from "../assets/logos/texas-rangers-logo.svg";
import JaysLogo from "../assets/logos/toronto-blue-jays-logo.svg";
import TwinsLogo from "../assets/logos/minnesota-twins-logo.svg";
import PhilliesLogo from "../assets/logos/philadelphia-phillies-logo.svg";
import BravesLogo from "../assets/logos/atlanta-braves-logo.svg";
import RedSoxLogo from "../assets/logos/boston-red-sox-logo.svg";
import MarlinsLogo from "../assets/logos/miami-marlins-logo.svg";
import YankeesLogo from "../assets/logos/new-york-yankees-logo.svg";
import BrewersLogo from "../assets/logos/milwaukee-brewers-logo.svg";
import AngelsLogo from "../assets/logos/los-angeles-angels-logo.svg";
import DiamondbacksLogo from "../assets/logos/arizona-diamondbacks-logo.svg";
import OriolesLogo from "../assets/logos/baltimore-orioles-logo.svg";
import WhiteSoxLogo from "../assets/logos/chicago-white-sox-logo.svg";
import CubsLogo from "../assets/logos/chicago-cubs-logo.svg";
import RedsLogo from "../assets/logos/cincinnati-reds-logo.svg";
import GuardiansLogo from "../assets/logos/cleveland-indians-logo.svg";
import RockiesLogo from "../assets/logos/colorado-rockies-logo.svg";
import TigersLogo from "../assets/logos/detroit-tigers-logo.svg";
import AstrosLogo from "../assets/logos/houston-astros-logo.svg";
import RoyalsLogo from "../assets/logos/kansas-city-royals-logo.svg";
import DodgersLogo from "../assets/logos/los-angeles-dodgers-logo.svg";
import NationalsLogo from "../assets/logos/washington-nationals-logo.svg";
import MetsLogo from "../assets/logos/new-york-mets-logo.svg";

export function getTeamColors(teamId: number): Record<string, string> {
  for (const team of mlbTeams) {
    if ("colors" in team && team["colors"] && teamId == team.id) {
      return team["colors"];
    }
  }

  return {};
}

export function getTeamName(teamId: number): Record<string, string> {
  for (const team of mlbTeams) {
    if (teamId === team.id) {
      return { name: team["name"] };
    }
  }

  return {};
}

export function getTeamLogo(teamId: number): string {
  switch (teamId) {
    case 133:
      return AthleticsLogo;
    case 134:
      return PiratesLogo;
    case 135:
      return PadresLogo;
    case 136:
      return MarinersLogo;
    case 137:
      return GiantsLogo;
    case 138:
      return CardinalsLogo;
    case 139:
      return RaysLogo;
    case 140:
      return RangersLogo;
    case 141:
      return JaysLogo;
    case 142:
      return TwinsLogo;
    case 143:
      return PhilliesLogo;
    case 144:
      return BravesLogo;
    case 145:
      return WhiteSoxLogo;
    case 146:
      return MarlinsLogo;
    case 147:
      return YankeesLogo;
    case 158:
      return BrewersLogo;
    case 108:
      return AngelsLogo;
    case 109:
      return DiamondbacksLogo;
    case 110:
      return OriolesLogo;
    case 111:
      return RedSoxLogo;
    case 112:
      return CubsLogo;
    case 113:
      return RedsLogo;
    case 114:
      return GuardiansLogo;
    case 115:
      return RockiesLogo;
    case 116:
      return TigersLogo;
    case 117:
      return AstrosLogo;
    case 118:
      return RoyalsLogo;
    case 119:
      return DodgersLogo;
    case 120:
      return NationalsLogo;
    case 121:
      return MetsLogo;
    default:
      return "";
  }
}
