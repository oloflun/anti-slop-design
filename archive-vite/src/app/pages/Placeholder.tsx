import { useLocale } from "../hooks/useLocale";
import { Link, useLocation } from "react-router";
import { ArrowLeft } from "lucide-react";

export function Placeholder() {
  const { t, locale } = useLocale();
  const location = useLocation();

  const getPageTitle = () => {
    switch (location.pathname) {
      case "/sortiment": return t("nav.assortment");
      case "/partners": return t("nav.partners");
      case "/om-oss": return t("nav.about");
      case "/kontakt": return t("nav.contact");
      default: return locale === 'sv' ? "Sida under uppbyggnad" : "Page Under Construction";
    }
  };

  return (
    <div className="flex-1 w-full bg-black flex flex-col items-center justify-center p-8 min-h-[50vh]">
      <div className="text-center max-w-2xl">
        <h1 
          className="text-4xl md:text-6xl font-black uppercase tracking-tighter text-white mb-6"
        >
          {getPageTitle()}
        </h1>
        <p className="text-xl font-light text-gray-400 mb-12">
          {locale === 'sv' 
            ? "Denna sektion är för närvarande under uppbyggnad och kommer att lanseras inom kort. Tack för ditt tålamod." 
            : "This section is currently under construction and will be launched shortly. Thank you for your patience."}
        </p>
        <Link 
          to="/" 
          className="inline-flex items-center text-[#F27722] font-bold uppercase tracking-widest hover:text-white transition-colors"
        >
          <ArrowLeft className="w-5 h-5 mr-2" />
          {locale === 'sv' ? "Tillbaka till startsidan" : "Back to Home"}
        </Link>
      </div>
    </div>
  );
}
