/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(164, 100%, 97%)',
            '100': 'hsl(164, 100%, 94%)',
            '200': 'hsl(164, 100%, 86%)',
            '300': 'hsl(164, 100%, 76%)',
            '400': 'hsl(164, 100%, 64%)',
            '500': 'hsl(164, 100%, 50%)',
            '600': 'hsl(164, 100%, 40%)',
            '700': 'hsl(164, 100%, 32%)',
            '800': 'hsl(164, 100%, 24%)',
            '900': 'hsl(164, 100%, 16%)',
            '950': 'hsl(164, 100%, 10%)',
            DEFAULT: '#00ffbb'
        },
        secondary: {
            '50': 'hsl(193, 49%, 97%)',
            '100': 'hsl(193, 49%, 94%)',
            '200': 'hsl(193, 49%, 86%)',
            '300': 'hsl(193, 49%, 76%)',
            '400': 'hsl(193, 49%, 64%)',
            '500': 'hsl(193, 49%, 50%)',
            '600': 'hsl(193, 49%, 40%)',
            '700': 'hsl(193, 49%, 32%)',
            '800': 'hsl(193, 49%, 24%)',
            '900': 'hsl(193, 49%, 16%)',
            '950': 'hsl(193, 49%, 10%)',
            DEFAULT: '#14323a'
        },
        accent: {
            '50': 'hsl(150, 100%, 97%)',
            '100': 'hsl(150, 100%, 94%)',
            '200': 'hsl(150, 100%, 86%)',
            '300': 'hsl(150, 100%, 76%)',
            '400': 'hsl(150, 100%, 64%)',
            '500': 'hsl(150, 100%, 50%)',
            '600': 'hsl(150, 100%, 40%)',
            '700': 'hsl(150, 100%, 32%)',
            '800': 'hsl(150, 100%, 24%)',
            '900': 'hsl(150, 100%, 16%)',
            '950': 'hsl(150, 100%, 10%)',
            DEFAULT: '#00ff7f'
        },
        'neutral-50': '#f6f5f3',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#979797',
        'neutral-400': '#cecece',
        'neutral-500': '#e2dfdf',
        background: '#1a4145',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Season Sans',
            'sans-serif'
        ],
        mono: [
            'Test Sohne Mono',
            'sans-serif'
        ],
        font2: [
            'Season Serif',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '16px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px'
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
                lineHeight: '18px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '31.2px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '64px',
                letterSpacing: '-0.9px'
            }
        ],
        '53': [
            '53px',
            {
                lineHeight: '60px',
                letterSpacing: '-1.325px'
            }
        ],
        '81': [
            '81px',
            {
                lineHeight: '89.1px',
                letterSpacing: '-2.187px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '12': '24px',
        '18': '36px',
        '24': '48px',
        '28': '56px',
        '30': '60px',
        '32': '64px',
        '40': '80px',
        '44': '88px',
        '56': '112px',
        '64': '128px',
        '80': '160px',
        '160': '320px',
        '175': '350px',
        '71px': '71px',
        '175px': '175px',
        '241px': '241px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '16px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 3px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 2px -1px'
    },
    screens: {
        md: '768px'
    },
    transitionDuration: {
        '150': '0.15s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0, 0, 0.2, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};
