import { createContext, useContext, useState, ReactNode } from 'react';

type Locale = 'sv' | 'en';

type Translations = Record<string, Record<Locale, string>>;

const translations: Translations = {
  'nav.home': { sv: 'Hem', en: 'Home' },
  'nav.assortment': { sv: 'Sortiment', en: 'Assortment' },
  'nav.brands': { sv: 'Varumärken', en: 'Brands' },
  'nav.partners': { sv: 'Samarbetspartners & Kunder', en: 'Partners & Customers' },
  'nav.about': { sv: 'Om oss', en: 'About Us' },
  'nav.contact': { sv: 'Kontakt', en: 'Contact' },
  'hero.title': { sv: 'Vi bygger dina varumärken.', en: 'We build your brands.' },
  'hero.subtitle': { 
    sv: 'Med ett brett sortiment över ett stort antal produktkategorier hjälper vi dig som återförsäljare att bygga starka varumärken, med över 100 leverantörer har vi något för alla!', 
    en: 'With a wide range across a large number of product categories, we help you as a retailer build strong brands. With over 100 suppliers, we have something for everyone!' 
  },
  'footer.seoText': {
    sv: 'Haajp Trading- bygger varumärken åt återförsäljare, eller Haajp Trading AB hjälper återförsäljare att bygga starka varumärken åt återförsäljare, med ett brett sortiment över ett stort antal produktkategorier.',
    en: 'Haajp Trading - building brands for retailers, or Haajp Trading AB helps retailers build strong brands for retailers, with a wide range across a large number of product categories.'
  },
  'footer.address': { sv: 'Adress:', en: 'Address:' },
  'footer.email': { sv: 'Epost:', en: 'Email:' },
  'footer.phone': { sv: 'Telefon:', en: 'Phone:' },
  'dropdown.retailers': { sv: 'Återförsäljare', en: 'Retailers' }
};

type LocaleContextType = {
  locale: Locale;
  toggleLocale: () => void;
  t: (key: string) => string;
};

const LocaleContext = createContext<LocaleContextType | undefined>(undefined);

export function LocaleProvider({ children }: { children: ReactNode }) {
  const [locale, setLocale] = useState<Locale>('sv');

  const toggleLocale = () => {
    setLocale((prev) => (prev === 'sv' ? 'en' : 'sv'));
  };

  const t = (key: string) => {
    return translations[key]?.[locale] || key;
  };

  return (
    <LocaleContext.Provider value={{ locale, toggleLocale, t }}>
      {children}
    </LocaleContext.Provider>
  );
}

export function useLocale() {
  const context = useContext(LocaleContext);
  if (!context) {
    throw new Error('useLocale must be used within a LocaleProvider');
  }
  return context;
}
