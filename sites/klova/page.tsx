"use client";

import React, { useState, useEffect, useRef } from 'react';
import Link from 'next/link';
import { Logo } from '@/src/components/Logo';
import { NavLink } from '@/src/components/NavLink';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronLeft, ChevronRight, Menu as MenuIcon, X } from 'lucide-react';

const slides = [
  { src: "/input_file0.png", alt: "Schnitzlar" },
  { src: "/input_file_7.png", alt: "Soppa" },
  { src: "/input_file_9.png", alt: "Räkor och mos" },
  { src: "/input_file_2.png", alt: "Champagne" },
  { src: "/input_file_4.png", alt: "Charkbricka" },
  { src: "/input_file_11.png", alt: "Schnitzel närbild" },
  { src: "/input_file_12.png", alt: "Sallad" },
  { src: "/input_file_6.png", alt: "Spett" },
  { src: "/input_file_5.png", alt: "Hamburgare" },
];

export default function Home() {
  const [scrolled, setScrolled] = useState(false);
  const [currentSlide, setCurrentSlide] = useState(0);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  // Försök tvinga igång videon om den inte startar
  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.muted = true;
      videoRef.current.play().catch(err => {
        console.warn("Video autoplay failed, user interaction might be needed", err);
      });
    }
  }, []);

  const nextSlide = () => setCurrentSlide((prev) => (prev + 1) % slides.length);
  const prevSlide = () => setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);

  return (
    <main className="min-h-screen">
      {/* Header */}
      <header 
        className={`fixed top-0 w-full z-50 transition-all duration-500 px-6 py-4 flex justify-between items-center ${
          scrolled ? 'bg-white/95 text-slate-900 shadow-md py-3' : 'bg-transparent text-white'
        }`}
      >
        <Link href="/">
          <Logo className="w-48" variant={scrolled ? 'black' : 'white'} />
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden md:flex gap-10 text-lg font-serif">
          <NavLink href="/">Hem</NavLink>
          <NavLink href="/meny">Meny</NavLink>
          <NavLink href="#om-oss">Om oss</NavLink>
          <NavLink href="#boka">Boka bord</NavLink>
        </nav>

        {/* Mobile Nav Toggle */}
        <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
          {isMenuOpen ? <X /> : <MenuIcon />}
        </button>
      </header>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
            <motion.div 
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="fixed inset-0 z-40 bg-white flex flex-col items-center justify-center gap-10 text-3xl font-serif"
            >
              <NavLink href="/" onClick={() => setIsMenuOpen(false)}>Hem</NavLink>
              <NavLink href="/meny" onClick={() => setIsMenuOpen(false)}>Meny</NavLink>
              <NavLink href="#om-oss" onClick={() => setIsMenuOpen(false)}>Om oss</NavLink>
              <NavLink href="#boka" onClick={() => setIsMenuOpen(false)}>Boka bord</NavLink>
            </motion.div>
        )}
      </AnimatePresence>

      {/* Hero Section */}
      <section className="relative h-screen flex items-center justify-center overflow-hidden bg-slate-900">
        <video 
          ref={videoRef}
          autoPlay 
          loop 
          muted 
          playsInline 
          className="absolute inset-0 w-full h-full object-cover opacity-60"
          poster="/building.png"
        >
          <source src="/input_file_8.mp4" type="video/mp4" />
          Din webbläsare stödjer inte HTML5-video.
        </video>
        
        <div className="relative z-10 text-center text-white px-4 max-w-4xl">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1 }}
          >
            <Logo className="mb-8 w-64 mx-auto" variant="white" />
            <h1 className="text-5xl md:text-7xl font-serif mb-6 drop-shadow-lg">
              Välkommen till Hamnen
            </h1>
            <p className="text-lg md:text-xl font-light mb-10 tracking-wide drop-shadow-md">
              Där saltstänk och matglädje möts. Njut av Västkustens finaste smaker precis vid havskanten.
            </p>
            <Link 
              href="/meny" 
              className="inline-block px-10 py-4 border border-white text-white uppercase tracking-[0.2em] text-sm hover:bg-white hover:text-slate-900 transition-all duration-300 backdrop-blur-sm"
            >
              Se vår meny
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Intro Section */}
      <section id="om-oss" className="py-24 px-6 bg-white overflow-hidden">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-2 gap-16 items-center">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 1 }}
              viewport={{ once: true }}
              className="relative h-[500px] rounded-2xl overflow-hidden shadow-2xl"
            >
              <img 
                src="/building.png" 
                alt="Klova Hamnkrog byggnad" 
                className="w-full h-full object-cover"
              />
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              transition={{ duration: 1 }}
              viewport={{ once: true }}
              className="text-left"
            >
              <h2 className="text-4xl md:text-5xl font-serif mb-8 text-slate-900 leading-tight">Välkommen till oss på kajen</h2>
              <div className="space-y-6 text-slate-600 leading-relaxed text-lg">
                <p>
                  Inspirerade av havets skafferi och lokala råvaror bjuder vi in till en restaurangupplevelse utöver det vanliga. Med utgångspunkt i svensk matkultur och en kärlek för noga utvalda ingredienser, lagar vi mat som värmer hjärtat.
                </p>
                <p>
                  Oavsett om du vill fira sommarkvällen med krispig champagne på uteserveringen, värma dig med en mustig skaldjurssoppa, eller njuta av en klassisk schnitzel – så har vi ett bord för dig. Slå dig ner och låt oss ta hand om dig.
                </p>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Gallery Section */}
      <section className="py-24 px-6 bg-[#f4ede4]">
        <div className="max-w-6xl mx-auto text-center mb-12">
          <h2 className="text-4xl font-serif text-slate-900">Glimtar från Hamnkrogen</h2>
        </div>

        <div className="relative max-w-5xl mx-auto aspect-[16/9] rounded-xl overflow-hidden shadow-2xl group">
          <AnimatePresence mode="wait">
            <motion.img
              key={currentSlide}
              src={slides[currentSlide].src}
              alt={slides[currentSlide].alt}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.8 }}
              className="w-full h-full object-cover"
            />
          </AnimatePresence>
          
          <button 
            onClick={prevSlide}
            className="absolute left-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 p-3 rounded-full backdrop-blur-md transition-all opacity-0 group-hover:opacity-100"
          >
            <ChevronLeft className="text-white" />
          </button>
          <button 
            onClick={nextSlide}
            className="absolute right-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 p-3 rounded-full backdrop-blur-md transition-all opacity-0 group-hover:opacity-100"
          >
            <ChevronRight className="text-white" />
          </button>

          <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex gap-2">
            {slides.map((_, i) => (
              <div 
                key={i} 
                className={`w-2 h-2 rounded-full transition-all ${i === currentSlide ? 'bg-white w-4' : 'bg-white/40'}`}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer id="boka" className="bg-slate-900 text-white py-20 px-6 text-center">
        <Logo className="mb-8 opacity-80 w-48 mx-auto" variant="white" />
        <div className="space-y-4 mb-12">
          <p className="text-xl font-serif">Öppet alla dagar från 11:30</p>
          <p className="text-slate-400">Telefon: 072-971 71 10 &nbsp; | &nbsp; E-post: info@nyakroken.se</p>
        </div>
        <div className="pt-12 border-t border-white/10 text-xs text-slate-500">
          &copy; 2026 Klova Hamnkrog. Följ oss gärna på Instagram och Facebook.
        </div>
      </footer>
    </main>
  );
}
