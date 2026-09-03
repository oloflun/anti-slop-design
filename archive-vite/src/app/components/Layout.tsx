import { Outlet, Link, useLocation } from "react-router";
import { useLocale } from "../hooks/useLocale";
import { Flag, ChevronDown, Menu, X } from "lucide-react";
import logoImage from "figma:asset/c40574c649471159cfd43f4896d910fb9a56ee26.png";
import { useState, useEffect } from "react";
import clsx from "clsx";

const brands = [
  "AEG", "Bosch", "Einhell", "Grundig", "Nordic Quality", 
  "Philips", "Panasonic", "Reservo", "Tefal", "Tyzon"
];

const retailers = [
  "Återförsäljare 1", "Återförsäljare 2", "MediaMarkt", "Elgiganten", "NetOnNet", "Elon", "Komplett"
];

function NavItem({ 
  to, 
  label, 
  dropdownItems, 
  dropdownTitle,
  mobile,
  closeMenu
}: { 
  to: string, 
  label: string, 
  dropdownItems?: string[], 
  dropdownTitle?: string,
  mobile?: boolean,
  closeMenu?: () => void
}) {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();
  const isActive = location.pathname === to || (to !== '/' && location.pathname.startsWith(to));

  if (mobile) {
    return (
      <div className="flex flex-col w-full border-b border-zinc-800/50 last:border-0">
        <div 
          className="flex items-center justify-between px-4 py-4"
          onClick={() => {
            if (dropdownItems) {
              setIsOpen(!isOpen);
            } else if (closeMenu) {
              closeMenu();
            }
          }}
        >
          <Link 
            to={to} 
            onClick={(e) => {
               if (dropdownItems) {
                 e.preventDefault();
               } else if (closeMenu) {
                 closeMenu();
               }
            }}
            className={clsx(
              "font-bold uppercase tracking-wider text-lg transition-colors",
              isActive ? "text-[#F27722]" : "text-white hover:text-[#F27722]"
            )}
          >
            {label}
          </Link>
          {dropdownItems && (
            <ChevronDown className={clsx("w-5 h-5 text-gray-400 transition-transform", isOpen && "rotate-180")} />
          )}
        </div>
        
        {dropdownItems && isOpen && (
          <div className="bg-zinc-900/50 pb-4">
            {dropdownTitle && (
              <div className="px-6 py-2 text-[#F27722] font-bold uppercase text-xs tracking-wider">
                {dropdownTitle}
              </div>
            )}
            <ul className="space-y-1">
              {dropdownItems.map((item, idx) => (
                <li key={idx}>
                  <Link 
                    to="#" 
                    className="block px-8 py-2 text-sm text-gray-300 hover:text-[#F27722]"
                    onClick={closeMenu}
                  >
                    {item}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    );
  }

  return (
    <div 
      className="relative group"
      onMouseEnter={() => setIsOpen(true)}
      onMouseLeave={() => setIsOpen(false)}
    >
      <Link 
        to={to} 
        className={clsx(
          "flex items-center gap-1 px-3 lg:px-4 py-2 font-bold text-white uppercase tracking-wider transition-all duration-300",
          "hover:scale-105 hover:text-[#F27722]",
          isActive && "text-[#F27722]",
          "text-sm lg:text-base"
        )}
      >
        {label}
        {dropdownItems && <ChevronDown className="w-4 h-4 text-gray-400 transition-transform group-hover:rotate-180 group-hover:text-[#F27722]" />}
      </Link>
      
      {dropdownItems && isOpen && (
        <div className="absolute top-full left-0 mt-0 pt-4 w-56 z-50">
          <div className="bg-zinc-900 border border-[#F27722] rounded shadow-2xl overflow-hidden">
            {dropdownTitle && (
              <div className="px-4 py-3 bg-[#F27722] text-black font-black uppercase text-xs tracking-widest">
                {dropdownTitle}
              </div>
            )}
            <ul className="py-2">
              {dropdownItems.map((item, idx) => (
                <li key={idx}>
                  <Link 
                    to="#" 
                    className="block px-4 py-2.5 text-sm text-gray-300 font-medium hover:bg-[#F27722] hover:text-black transition-colors"
                  >
                    {item}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export function Layout() {
  const { t, toggleLocale, locale } = useLocale();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Close mobile menu when locale changes
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [locale]);

  useEffect(() => {
    document.title = locale === 'sv' 
      ? 'Haajp Trading AB - bygger varumärken åt återförsäljare'
      : 'Haajp Trading AB - building brands for retailers';
    
    let metaDescription = document.querySelector('meta[name="description"]');
    if (!metaDescription) {
      metaDescription = document.createElement('meta');
      metaDescription.setAttribute('name', 'description');
      document.head.appendChild(metaDescription);
    }
    metaDescription.setAttribute('content', t('footer.seoText'));
  }, [locale, t]);

  return (
    <div className="min-h-screen flex flex-col bg-black text-white font-sans selection:bg-[#F27722] selection:text-black">
      <header className="sticky top-0 z-50 w-full bg-black/95 backdrop-blur-md border-b border-zinc-800 shadow-xl">
        <div className="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-24 md:h-32">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center h-full">
              <Link to="/" className="group flex items-center h-[75%]">
                <img 
                  src={logoImage} 
                  alt="Haajp Trading AB Logo" 
                  className="h-full w-auto object-contain transition-transform duration-300 group-hover:scale-105"
                />
              </Link>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden lg:flex flex-1 justify-center items-center space-x-4 xl:space-x-6">
              <NavItem to="/" label={t('nav.home')} />
              <NavItem 
                to="/sortiment" 
                label={t('nav.assortment')} 
                dropdownItems={brands}
                dropdownTitle={t('nav.brands')}
              />
              <NavItem 
                to="/partners" 
                label={t('nav.partners')} 
                dropdownItems={retailers}
                dropdownTitle={t('dropdown.retailers')}
              />
              <NavItem to="/om-oss" label={t('nav.about')} />
              <NavItem to="/kontakt" label={t('nav.contact')} />
            </nav>

            {/* Right side controls */}
            <div className="flex items-center gap-4 lg:pl-4">
              {/* Language Toggle */}
              <button 
                onClick={toggleLocale}
                className="flex items-center gap-2 px-3 py-2 text-gray-300 hover:text-[#F27722] transition-colors rounded hover:bg-white/5"
                aria-label="Toggle Language"
              >
                <Flag className="w-5 h-5" />
                <span className="text-sm font-bold uppercase tracking-wider">{locale === 'sv' ? 'EN' : 'SV'}</span>
              </button>

              {/* Mobile Menu Button */}
              <button
                className="lg:hidden p-2 text-gray-300 hover:text-[#F27722] transition-colors"
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                aria-label="Toggle Menu"
              >
                {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <div className="lg:hidden absolute top-full left-0 w-full bg-black/95 backdrop-blur-xl border-b border-zinc-800 shadow-2xl max-h-[calc(100vh-96px)] overflow-y-auto">
            <nav className="flex flex-col w-full max-w-md mx-auto py-4">
              <NavItem to="/" label={t('nav.home')} mobile closeMenu={() => setMobileMenuOpen(false)} />
              <NavItem 
                to="/sortiment" 
                label={t('nav.assortment')} 
                dropdownItems={brands}
                dropdownTitle={t('nav.brands')}
                mobile 
                closeMenu={() => setMobileMenuOpen(false)}
              />
              <NavItem 
                to="/partners" 
                label={t('nav.partners')} 
                dropdownItems={retailers}
                dropdownTitle={t('dropdown.retailers')}
                mobile 
                closeMenu={() => setMobileMenuOpen(false)}
              />
              <NavItem to="/om-oss" label={t('nav.about')} mobile closeMenu={() => setMobileMenuOpen(false)} />
              <NavItem to="/kontakt" label={t('nav.contact')} mobile closeMenu={() => setMobileMenuOpen(false)} />
            </nav>
          </div>
        )}
      </header>

      <main className="flex-1 w-full flex flex-col items-center">
        <Outlet />
      </main>

      <footer className="w-full bg-black text-gray-400 py-16 border-t border-zinc-900">
        <div className="max-w-[1400px] w-full mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
            
            {/* About Column */}
            <div className="flex flex-col items-start">
              <img src={logoImage} alt="Haajp Trading AB Logo" className="h-10 w-auto mb-6 opacity-90" />
              <p className="text-sm leading-relaxed mb-6 font-light max-w-sm">
                {t('footer.seoText')}
              </p>
            </div>
            
            {/* Contact Column */}
            <div>
              <h3 className="text-white font-black text-lg mb-6 text-[#F27722] uppercase tracking-widest">
                {t('nav.contact')}
              </h3>
              <ul className="space-y-4 text-sm font-medium">
                <li className="flex flex-col">
                  <span className="font-bold text-gray-300 uppercase text-xs tracking-wider mb-1">{t('footer.address')}</span>
                  <span className="text-gray-400">Kärra 387, 463 95 Lödöse</span>
                </li>
                <li className="flex flex-col">
                  <span className="font-bold text-gray-300 uppercase text-xs tracking-wider mb-1">{t('footer.email')}</span>
                  <a href="mailto:haajp-trading@outlook.com" className="text-gray-400 hover:text-[#F27722] transition-colors">
                    haajp-trading@outlook.com
                  </a>
                </li>
                <li className="flex flex-col">
                  <span className="font-bold text-gray-300 uppercase text-xs tracking-wider mb-1">{t('footer.phone')}</span>
                  <a href="tel:0706889072" className="text-gray-400 hover:text-[#F27722] transition-colors">
                    070-688 90 72
                  </a>
                </li>
              </ul>
            </div>
            
            {/* Links Column */}
            <div>
               <h3 className="text-white font-black text-lg mb-6 text-[#F27722] uppercase tracking-widest">
                {locale === 'sv' ? 'Snabblänkar' : 'Quick Links'}
              </h3>
              <ul className="space-y-3 text-sm font-medium">
                <li>
                  <Link to="/" className="text-gray-400 hover:text-[#F27722] hover:pl-2 transition-all block">
                    {t('nav.home')}
                  </Link>
                </li>
                <li>
                  <Link to="/sortiment" className="text-gray-400 hover:text-[#F27722] hover:pl-2 transition-all block">
                    {t('nav.assortment')}
                  </Link>
                </li>
                <li>
                  <Link to="/partners" className="text-gray-400 hover:text-[#F27722] hover:pl-2 transition-all block">
                    {t('nav.partners')}
                  </Link>
                </li>
                <li>
                  <Link to="/om-oss" className="text-gray-400 hover:text-[#F27722] hover:pl-2 transition-all block">
                    {t('nav.about')}
                  </Link>
                </li>
                <li>
                  <Link to="/kontakt" className="text-gray-400 hover:text-[#F27722] hover:pl-2 transition-all block">
                    {t('nav.contact')}
                  </Link>
                </li>
              </ul>
            </div>
          </div>
          
          <div className="mt-16 pt-8 border-t border-zinc-900 text-center flex flex-col md:flex-row justify-between items-center text-xs font-medium text-zinc-600">
            <p>&copy; {new Date().getFullYear()} Haajp Trading AB. {locale === 'sv' ? 'Alla rättigheter förbehållna.' : 'All rights reserved.'}</p>
            <p className="mt-2 md:mt-0">{locale === 'sv' ? 'Bygger varumärken för framtiden.' : 'Building brands for the future.'}</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
