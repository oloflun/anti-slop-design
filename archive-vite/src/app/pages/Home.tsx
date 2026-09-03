import { useLocale } from "../hooks/useLocale";
import heroImage from "figma:asset/c68138b4ae0e33a30ae31f8cbca7e3ce1ad14594.png";
import tyzonImage from "figma:asset/75845c9dc5ab353faaddb6d652b60ce296436d50.png";
import cablesImage from "figma:asset/58617d03422ee71e52a34576362ebde04ffd94f9.png";
import einhellImage from "figma:asset/a6d1b6482213220f5b66dca265149e78c55be640.png";
import { Link } from "react-router";
import { ArrowRight } from "lucide-react";

export function Home() {
  const { t, locale } = useLocale();

  return (
    <div className="flex-1 w-full bg-black flex flex-col items-center">
      
      {/* Hero Section */}
      <section className="w-full relative h-[60vh] md:h-[80vh] min-h-[500px] flex items-center justify-center overflow-hidden group">
        {/* Hero Background */}
        <div className="absolute inset-0 w-full h-full z-0">
          <img 
            src={heroImage} 
            alt="Wall of phone cases" 
            className="w-full h-full object-cover opacity-70 transition-transform duration-[1500ms] ease-out group-hover:scale-110"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-black/20"></div>
        </div>
        
        {/* Hero Text */}
        <div className="relative z-10 w-full max-w-5xl mx-auto px-4 text-center flex flex-col items-center mt-12 md:mt-16 pointer-events-none">
          <h1 
            className="text-5xl md:text-7xl lg:text-8xl font-black text-white uppercase tracking-tight mb-6 drop-shadow-2xl"
          >
            {t('hero.title')}
          </h1>
          <p className="text-xl md:text-3xl font-light text-gray-200 leading-relaxed max-w-3xl drop-shadow-lg">
            {t('hero.subtitle')}
          </p>
        </div>
      </section>

      {/* Categories / Showcase Section */}
      <section className="w-full max-w-7xl mx-auto py-24 px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 
            className="text-3xl md:text-4xl font-black uppercase tracking-widest text-[#F27722]"
          >
            {locale === 'sv' ? 'Vårt utbud' : 'Our Selection'}
          </h2>
          <div className="w-24 h-1 bg-[#F27722] mx-auto mt-6 rounded-full"></div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Card 1 */}
          <div className="group relative rounded-xl overflow-hidden border border-zinc-800 bg-black transition-all hover:-translate-y-2 hover:shadow-2xl hover:shadow-[#F27722]/20">
            <div className="aspect-square w-full overflow-hidden bg-black">
               <img 
                src={einhellImage} 
                alt="Einhell tools display" 
                className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-500 group-hover:scale-110"
              />
            </div>
            <div className="p-6 relative">
              <h3 className="text-xl font-bold uppercase text-white mb-2 group-hover:text-[#F27722] transition-colors">
                {locale === 'sv' ? 'Verktyg & Maskiner' : 'Tools & Machinery'}
              </h3>
              <p className="text-sm text-gray-400 mb-6">
                {locale === 'sv' 
                  ? 'Stort sortiment av kvalitetsverktyg från ledande varumärken som Einhell.'
                  : 'Large selection of quality tools from leading brands like Einhell.'}
              </p>
              <Link to="/sortiment" className="inline-flex items-center text-[#F27722] font-semibold text-sm hover:text-white transition-colors">
                {locale === 'sv' ? 'Utforska' : 'Explore'} <ArrowRight className="w-4 h-4 ml-2" />
              </Link>
            </div>
          </div>

          {/* Card 2 */}
          <div className="group relative rounded-xl overflow-hidden border border-zinc-800 bg-black transition-all hover:-translate-y-2 hover:shadow-2xl hover:shadow-[#F27722]/20">
            <div className="aspect-square w-full overflow-hidden bg-black">
               <img 
                src={tyzonImage} 
                alt="Tyzon batteries display" 
                className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-500 group-hover:scale-110"
              />
            </div>
            <div className="p-6 relative">
              <h3 className="text-xl font-bold uppercase text-white mb-2 group-hover:text-[#F27722] transition-colors">
                {locale === 'sv' ? 'Batterier & Ström' : 'Batteries & Power'}
              </h3>
              <p className="text-sm text-gray-400 mb-6">
                 {locale === 'sv' 
                  ? 'Kompletta lösningar för energi och strömförsörjning med varumärken som Tyzon.'
                  : 'Complete energy and power supply solutions with brands like Tyzon.'}
              </p>
              <Link to="/sortiment" className="inline-flex items-center text-[#F27722] font-semibold text-sm hover:text-white transition-colors">
                 {locale === 'sv' ? 'Utforska' : 'Explore'} <ArrowRight className="w-4 h-4 ml-2" />
              </Link>
            </div>
          </div>

          {/* Card 3 */}
          <div className="group relative rounded-xl overflow-hidden border border-zinc-800 bg-black transition-all hover:-translate-y-2 hover:shadow-2xl hover:shadow-[#F27722]/20">
            <div className="aspect-square w-full overflow-hidden bg-black">
               <img 
                src={cablesImage} 
                alt="Cables and accessories display" 
                className="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-500 group-hover:scale-110"
              />
            </div>
            <div className="p-6 relative">
              <h3 className="text-xl font-bold uppercase text-white mb-2 group-hover:text-[#F27722] transition-colors">
                {locale === 'sv' ? 'Mobiltillbehör' : 'Mobile Accessories'}
              </h3>
              <p className="text-sm text-gray-400 mb-6">
                {locale === 'sv' 
                  ? 'Kablar, laddare och skydd för alla typer av enheter.'
                  : 'Cables, chargers, and protection for all types of devices.'}
              </p>
              <Link to="/sortiment" className="inline-flex items-center text-[#F27722] font-semibold text-sm hover:text-white transition-colors">
                 {locale === 'sv' ? 'Utforska' : 'Explore'} <ArrowRight className="w-4 h-4 ml-2" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="w-full bg-[#F27722] text-black py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl md:text-5xl font-black uppercase tracking-tight mb-8">
            {locale === 'sv' ? 'Vill du bli återförsäljare?' : 'Want to become a retailer?'}
          </h2>
          <p className="text-lg font-medium mb-10 max-w-2xl mx-auto opacity-90">
             {locale === 'sv' 
              ? 'Kontakta oss idag för att få tillgång till vårt breda sortiment och börja bygga dina varumärken tillsammans med oss.'
              : 'Contact us today to get access to our wide range and start building your brands with us.'}
          </p>
          <Link 
            to="/kontakt" 
            className="inline-flex items-center justify-center px-8 py-4 bg-black text-white font-bold uppercase tracking-wider rounded-none hover:bg-zinc-800 transition-colors shadow-xl hover:scale-105 duration-300"
          >
            {t('nav.contact')} <ArrowRight className="w-5 h-5 ml-2" />
          </Link>
        </div>
      </section>
    </div>
  );
}
