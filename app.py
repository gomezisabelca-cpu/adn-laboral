import React, { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import CompanyChatInterface from './components/CompanyChatInterface';
import MatchGallery from './components/MatchGallery';
import { Sparkles, Fingerprint, BrainCircuit, HeartPulse, Building2, User, Target, ShieldCheck } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { Button } from '@/components/ui/button';

export default function App() {
  const [mode, setMode] = useState<'persona' | 'empresa'>('persona');
  const [view, setView] = useState<'chat' | 'matches'>('chat');

  return (
    <div className="min-h-screen bg-background flex flex-col">
      {/* Header */}
      <header className="py-6 px-6 border-b border-primary/10 bg-white/30 backdrop-blur-md sticky top-0 z-10">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className={`w-12 h-12 rounded-2xl flex items-center justify-center shadow-lg rotate-3 transition-colors duration-500 ${
              mode === 'persona' ? 'bg-primary shadow-primary/20' : 'bg-indigo-600 shadow-indigo-200'
            }`}>
              {mode === 'persona' ? <Fingerprint className="w-7 h-7 text-white" /> : <Building2 className="w-7 h-7 text-white" />}
            </div>
            <div>
              <h1 className={`text-3xl font-serif font-bold tracking-tight transition-colors duration-500 ${
                mode === 'persona' ? 'text-primary' : 'text-indigo-900'
              }`}>
                Mapeador de ADN Laboral
              </h1>
              <p className="text-sm font-sans text-muted-foreground uppercase tracking-[0.2em] font-medium">
                {mode === 'persona' ? 'Auditoría de Identidad Profesional' : 'Diseño de Cargos con Propósito'}
              </p>
            </div>
          </div>
          
          <div className="flex flex-col sm:flex-row gap-4 items-center">
            <div className="flex bg-muted p-1 rounded-full border border-border">
              <Button
                variant={view === 'chat' ? 'default' : 'ghost'}
                size="sm"
                onClick={() => setView('chat')}
                className={`rounded-full px-6 transition-all ${view === 'chat' ? '' : 'text-muted-foreground'}`}
              >
                Auditoría
              </Button>
              <Button
                variant={view === 'matches' ? 'default' : 'ghost'}
                size="sm"
                onClick={() => setView('matches')}
                className={`rounded-full px-6 transition-all ${view === 'matches' ? 'bg-primary text-white' : 'text-muted-foreground'}`}
              >
                Matches
              </Button>
            </div>

            <div className="flex bg-muted p-1 rounded-full border border-border">
              <Button
                variant={mode === 'persona' ? 'default' : 'ghost'}
                size="sm"
                onClick={() => setMode('persona')}
                className={`rounded-full px-6 transition-all ${mode === 'persona' ? '' : 'text-muted-foreground'}`}
              >
                <User className="w-4 h-4 mr-2" />
                Personas
              </Button>
              <Button
                variant={mode === 'empresa' ? 'default' : 'ghost'}
                size="sm"
                onClick={() => setMode('empresa')}
                className={`rounded-full px-6 transition-all ${mode === 'empresa' ? 'bg-indigo-600 hover:bg-indigo-700' : 'text-muted-foreground'}`}
              >
                <Building2 className="w-4 h-4 mr-2" />
                Empresas
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-6 md:p-12">
        <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12">
          {/* Left Column: Intro & Stats */}
          <div className="lg:col-span-4 space-y-8">
            <AnimatePresence mode="wait">
              <motion.div 
                key={`${mode}-${view}`}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.4 }}
                className="space-y-4"
              >
                <h2 className={`text-4xl font-serif leading-tight ${mode === 'empresa' ? 'text-indigo-950' : ''}`}>
                  {view === 'matches' ? (
                    <>Tus conexiones de <br/><span className="italic text-primary">ADN Real.</span></>
                  ) : mode === 'persona' ? (
                    <>Tu valor no es un cargo, <br/><span className="italic text-primary">es tu esencia.</span></>
                  ) : (
                    <>Un cargo no es una lista, <br/><span className="italic text-indigo-600">es un propósito.</span></>
                  )}
                </h2>
                <p className="text-muted-foreground leading-relaxed">
                  {view === 'matches' 
                    ? "Aquí verás los perfiles que mejor encajan con tu ADN. No buscamos palabras clave, buscamos afinidad real en el propósito y la cultura."
                    : mode === 'persona' 
                      ? "Olvídate de las descripciones genéricas de LinkedIn. Vamos a desglosar tus experiencias para encontrar los verbos de acción que realmente te definen."
                      : "Deja de publicar vacantes exageradas. Vamos a destilar lo que realmente necesita tu equipo para que el talento correcto se sienta atraído por la verdad."}
                </p>
              </motion.div>
            </AnimatePresence>

            <div className="grid grid-cols-1 gap-4">
              {(mode === 'persona' ? [
                { icon: BrainCircuit, title: "Habilidades Latentes", desc: "Lo que haces bien sin darte cuenta." },
                { icon: HeartPulse, title: "Zonas de Flujo", desc: "Donde el tiempo desaparece." },
                { icon: Sparkles, title: "Traducción de Valor", desc: "Tu fortaleza en palabras reales." }
              ] : [
                { icon: Target, title: "Propósito Real", desc: "El problema que el cargo viene a resolver." },
                { icon: ShieldCheck, title: "Filtro de Honestidad", desc: "Lo que NO necesitas para el éxito." },
                { icon: Building2, title: "Cultura de Equipo", desc: "El entorno donde el talento brilla." }
              ]).map((item, i) => (
                <motion.div 
                  key={`${mode}-${i}`}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 + i * 0.1 }}
                  className={`p-4 rounded-2xl bg-white/60 border shadow-sm flex gap-4 items-start ${
                    mode === 'persona' ? 'border-primary/5' : 'border-indigo-100'
                  }`}
                >
                  <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${
                    mode === 'persona' ? 'bg-primary/10 text-primary' : 'bg-indigo-100 text-indigo-600'
                  }`}>
                    <item.icon className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className={`font-serif font-semibold ${mode === 'persona' ? 'text-primary' : 'text-indigo-900'}`}>{item.title}</h3>
                    <p className="text-xs text-muted-foreground">{item.desc}</p>
                  </div>
                </motion.div>
              ))}
            </div>

            <div className="pt-8 border-t border-primary/10">
              <p className={`text-[10px] uppercase tracking-[0.3em] font-bold mb-4 ${
                mode === 'persona' ? 'text-primary/40' : 'text-indigo-400'
              }`}>
                Metodología
              </p>
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs">
                  <span>{mode === 'persona' ? 'Auditoría de Diálogo' : 'Diseño de Cargo'}</span>
                  <span className={`font-mono ${mode === 'persona' ? 'text-primary' : 'text-indigo-600'}`}>Fase Activa</span>
                </div>
                <div className={`w-full h-1 rounded-full overflow-hidden ${mode === 'persona' ? 'bg-primary/10' : 'bg-indigo-100'}`}>
                  <div className={`w-1/3 h-full transition-all duration-1000 ${mode === 'persona' ? 'bg-primary' : 'bg-indigo-600'}`} />
                </div>
              </div>
            </div>
          </div>

          {/* Right Column: Chat or Matches */}
          <div className="lg:col-span-8">
            <AnimatePresence mode="wait">
              <motion.div
                key={`${mode}-${view}`}
                initial={{ opacity: 0, scale: 0.98 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.98 }}
                transition={{ duration: 0.3 }}
              >
                {view === 'matches' ? (
                  <MatchGallery mode={mode} />
                ) : mode === 'persona' ? (
                  <ChatInterface />
                ) : (
                  <CompanyChatInterface />
                )}
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="py-8 px-6 border-t border-primary/5 bg-white/20 backdrop-blur-sm">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
          <div className="flex items-center gap-2 text-muted-foreground/60">
            <Sparkles className="w-4 h-4" />
            <span className="text-[10px] font-bold uppercase tracking-widest">ADN Laboral © 2026</span>
          </div>
          
          <div className="group flex items-center gap-3 px-5 py-2.5 rounded-2xl bg-white/50 border border-primary/10 shadow-sm hover:shadow-md transition-all duration-300">
            <div className="w-9 h-9 rounded-full bg-primary/10 flex items-center justify-center">
              <HeartPulse className="w-5 h-5 text-primary animate-pulse" />
            </div>
            <div className="flex flex-col">
              <span className="text-[9px] uppercase tracking-tighter text-muted-foreground font-bold leading-none mb-1">Creado con propósito por</span>
              <span className="text-sm font-serif font-bold text-primary group-hover:text-primary/80 transition-colors leading-none">
                Isabel Gomez <span className="text-muted-foreground/30 font-sans font-normal mx-1">|</span> <span className="text-[11px] font-sans font-medium text-indigo-600/70">Ing. Civil / SEO Specialist</span>
              </span>
            </div>
          </div>
          
          <p className="text-[10px] uppercase tracking-widest text-muted-foreground/40 font-medium">
            Consultoría Organizacional & IA
          </p>
        </div>
      </footer>
    </div>
  );
}
