import { RouterProvider } from "react-router";
import { router } from "./routes";
import { LocaleProvider } from "./hooks/useLocale";

export default function App() {
  return (
    <LocaleProvider>
      <RouterProvider router={router} />
    </LocaleProvider>
  );
}
