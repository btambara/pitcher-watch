import { test, expect } from "vitest";
import { mount } from "@vue/test-utils";
import PlayerDetails from "../../components/PlayerDetails.vue";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

test("mount PlayerDetails component", async () => {
  expect(PlayerDetails).toBeTruthy();

  const wrapper = mount(PlayerDetails, {
    props: {
      fullName: "Major Leaguer",
      primaryNumber: "2",
      primaryPosition: "P",
      logo: "",
      currentTeamId: 1,
    },
    global: {
      components: {
        PlayerDetails,
      },
      plugins: [vuetify],
    },
  });

  expect(wrapper.text()).toContain("Major Leaguer #2 | P");
});
