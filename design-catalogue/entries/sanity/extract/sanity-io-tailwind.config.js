/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(219, 100%, 97%)',
            '100': 'hsl(219, 100%, 94%)',
            '200': 'hsl(219, 100%, 86%)',
            '300': 'hsl(219, 100%, 76%)',
            '400': 'hsl(219, 100%, 64%)',
            '500': 'hsl(219, 100%, 50%)',
            '600': 'hsl(219, 100%, 40%)',
            '700': 'hsl(219, 100%, 32%)',
            '800': 'hsl(219, 100%, 24%)',
            '900': 'hsl(219, 100%, 16%)',
            '950': 'hsl(219, 100%, 10%)',
            DEFAULT: '#0052ef'
        },
        secondary: {
            '50': 'hsl(212, 100%, 97%)',
            '100': 'hsl(212, 100%, 94%)',
            '200': 'hsl(212, 100%, 86%)',
            '300': 'hsl(212, 100%, 76%)',
            '400': 'hsl(212, 100%, 64%)',
            '500': 'hsl(212, 100%, 50%)',
            '600': 'hsl(212, 100%, 40%)',
            '700': 'hsl(212, 100%, 32%)',
            '800': 'hsl(212, 100%, 24%)',
            '900': 'hsl(212, 100%, 16%)',
            '950': 'hsl(212, 100%, 10%)',
            DEFAULT: '#9ecbff'
        },
        accent: {
            '50': 'hsl(20, 100%, 97%)',
            '100': 'hsl(20, 100%, 94%)',
            '200': 'hsl(20, 100%, 86%)',
            '300': 'hsl(20, 100%, 76%)',
            '400': 'hsl(20, 100%, 64%)',
            '500': 'hsl(20, 100%, 50%)',
            '600': 'hsl(20, 100%, 40%)',
            '700': 'hsl(20, 100%, 32%)',
            '800': 'hsl(20, 100%, 24%)',
            '900': 'hsl(20, 100%, 16%)',
            '950': 'hsl(20, 100%, 10%)',
            DEFAULT: '#ff5500'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#0b0b0b',
        'neutral-200': '#e1e4e8',
        'neutral-300': '#000000',
        'neutral-400': '#797979',
        'neutral-500': '#b9b9b9',
        'neutral-600': '#353535',
        'neutral-700': '#212121',
        'neutral-800': '#6a737d',
        'neutral-900': '#4a4a4a',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Waldenburg-75357948a2b6a39b',
            'sans-serif'
        ],
        mono: [
            'IBM Plex Mono-c20ba633a65a8c57',
            'sans-serif'
        ],
        body: [
            'Helvetica',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '13px'
            }
        ],
        '11': [
            '11px',
            {
                lineHeight: '16.5px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '18px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '16.9px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '19.5px',
                letterSpacing: '-0.15px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '23.4px',
                letterSpacing: '-0.18px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '22px',
                letterSpacing: '-0.2px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '26.4px',
                letterSpacing: '-0.24px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '35.2px',
                letterSpacing: '-0.32px'
            }
        ],
        '38': [
            '38px',
            {
                lineHeight: '41.8px',
                letterSpacing: '-1.14px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '51.6px',
                letterSpacing: '-1.68px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '48px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '72px',
                letterSpacing: '-2.88px'
            }
        ],
        '112': [
            '112px',
            {
                lineHeight: '112px',
                letterSpacing: '-4.48px'
            }
        ]
    },
    spacing: {
        '16': '32px',
        '24': '48px',
        '32': '64px',
        '45': '90px',
        '58': '116px',
        '74': '148px',
        '128': '256px',
        '139': '278px',
        '170': '340px',
        '1px': '1px',
        '103px': '103px',
        '127px': '127px',
        '161px': '161px',
        '233px': '233px'
    },
    borderRadius: {
        sm: '3px',
        md: '6px',
        lg: '11px',
        full: '99999px'
    },
    boxShadow: {
        sm: 'rgb(53, 53, 53) 0px 0px 0px 1px inset'
    },
    screens: {
        xs: '376px',
        md: '768px'
    },
    transitionDuration: {
        '0': '0s',
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        linear: 'linear',
        default: 'ease',
        custom: 'cubic-bezier(0.4, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '24px'
    },
    maxWidth: {
        container: '320px'
    }
},
  },
};
