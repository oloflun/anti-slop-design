import { useLocale } from "../hooks/useLocale";
import { Mail, Phone, MapPin } from "lucide-react";

export function Contact() {
  const { t, locale } = useLocale();

  return (
    <div className="flex-1 w-full bg-black min-h-[60vh] py-24 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        
        <div className="text-center mb-16">
          <h1 
            className="text-4xl md:text-5xl font-black uppercase tracking-tighter text-white mb-6"
          >
            {t('nav.contact')}
          </h1>
          <div className="w-24 h-1 bg-[#F27722] mx-auto rounded-full mb-8"></div>
          <p className="text-xl font-light text-gray-400 max-w-2xl mx-auto">
            {locale === 'sv' 
              ? "Tveka inte att höra av dig om du har några frågor eller vill bli återförsäljare." 
              : "Do not hesitate to contact us if you have any questions or want to become a retailer."}
          </p>
        </div>

        <div className="bg-black border border-zinc-800 rounded-2xl p-8 md:p-12 shadow-2xl shadow-black/50 grid grid-cols-1 md:grid-cols-3 gap-12 text-center md:text-left">
          
          <div className="flex flex-col items-center md:items-start group">
            <div className="w-16 h-16 rounded-full bg-[#F27722]/10 flex items-center justify-center mb-6 group-hover:bg-[#F27722] transition-colors duration-300">
              <MapPin className="w-8 h-8 text-[#F27722] group-hover:text-black transition-colors" />
            </div>
            <h3 className="text-xl font-bold uppercase text-white mb-4">{t('footer.address')}</h3>
            <p className="text-gray-400 text-lg">
              Kärra 387<br />
              463 95 Lödöse
            </p>
          </div>

          <div className="flex flex-col items-center md:items-start group">
            <div className="w-16 h-16 rounded-full bg-[#F27722]/10 flex items-center justify-center mb-6 group-hover:bg-[#F27722] transition-colors duration-300">
              <Mail className="w-8 h-8 text-[#F27722] group-hover:text-black transition-colors" />
            </div>
            <h3 className="text-xl font-bold uppercase text-white mb-4">{t('footer.email')}</h3>
            <a 
              href="mailto:haajp-trading@outlook.com" 
              className="text-[#F27722] text-lg hover:text-white transition-colors break-all"
            >
              haajp-trading@outlook.com
            </a>
          </div>

          <div className="flex flex-col items-center md:items-start group">
            <div className="w-16 h-16 rounded-full bg-[#F27722]/10 flex items-center justify-center mb-6 group-hover:bg-[#F27722] transition-colors duration-300">
              <Phone className="w-8 h-8 text-[#F27722] group-hover:text-black transition-colors" />
            </div>
            <h3 className="text-xl font-bold uppercase text-white mb-4">{t('footer.phone')}</h3>
            <a 
              href="tel:0706889072" 
              className="text-[#F27722] text-lg hover:text-white transition-colors"
            >
              070-688 90 72
            </a>
          </div>

        </div>

      </div>
    </div>
  );
}
