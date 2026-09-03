import { createBrowserRouter } from "react-router";
import { Layout } from "./components/Layout";
import { Home } from "./pages/Home";
import { Placeholder } from "./pages/Placeholder";
import { Contact } from "./pages/Contact";

export const router = createBrowserRouter([
  {
    path: "/",
    Component: Layout,
    children: [
      { index: true, Component: Home },
      { path: "sortiment", Component: Placeholder },
      { path: "partners", Component: Placeholder },
      { path: "om-oss", Component: Placeholder },
      { path: "kontakt", Component: Contact },
      { path: "*", Component: Placeholder },
    ],
  },
]);
