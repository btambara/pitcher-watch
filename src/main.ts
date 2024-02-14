import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

// Font Awesome
import "@fortawesome/fontawesome-free/css/all.css";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import { aliases, fa } from "vuetify/iconsets/fa";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  defaults: {
    data: {
      tab: "one",
    },
  },
  icons: {
    defaultSet: "fa",
    aliases,
    sets: {
      fa,
    },
  },
  components,
  directives,
});

createApp(App).use(vuetify).mount("#app");
