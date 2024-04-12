import { expect, test } from "vitest";
import { getTeamColors, getTeamName, getTeamLogo } from "../helpers/index";

test("test getTeamColors", () => {
  const expected = {
    first: "#003831",
    forth: "",
    second: "#EFB21E",
    third: "#A2AAAD",
  };
  expect(getTeamColors(133)).toStrictEqual(expected);
});

test("test getTeamName", () => {
  const expected = {
    name: "Oakland Athletics",
  };
  expect(getTeamName(133)).toStrictEqual(expected);
});

test("test getTeamLogo", () => {
  expect(getTeamLogo(133)).toBe("/src/assets/logos/oakland-athletics-logo.svg");
});
