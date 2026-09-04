/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(221, 100%, 97%)',
            '100': 'hsl(221, 100%, 94%)',
            '200': 'hsl(221, 100%, 86%)',
            '300': 'hsl(221, 100%, 76%)',
            '400': 'hsl(221, 100%, 64%)',
            '500': 'hsl(221, 100%, 50%)',
            '600': 'hsl(221, 100%, 40%)',
            '700': 'hsl(221, 100%, 32%)',
            '800': 'hsl(221, 100%, 24%)',
            '900': 'hsl(221, 100%, 16%)',
            '950': 'hsl(221, 100%, 10%)',
            DEFAULT: '#3d7cff'
        },
        secondary: {
            '50': 'hsl(127, 84%, 97%)',
            '100': 'hsl(127, 84%, 94%)',
            '200': 'hsl(127, 84%, 86%)',
            '300': 'hsl(127, 84%, 76%)',
            '400': 'hsl(127, 84%, 64%)',
            '500': 'hsl(127, 84%, 50%)',
            '600': 'hsl(127, 84%, 40%)',
            '700': 'hsl(127, 84%, 32%)',
            '800': 'hsl(127, 84%, 24%)',
            '900': 'hsl(127, 84%, 16%)',
            '950': 'hsl(127, 84%, 10%)',
            DEFAULT: '#0fa821'
        },
        accent: {
            '50': 'hsl(216, 96%, 97%)',
            '100': 'hsl(216, 96%, 94%)',
            '200': 'hsl(216, 96%, 86%)',
            '300': 'hsl(216, 96%, 76%)',
            '400': 'hsl(216, 96%, 64%)',
            '500': 'hsl(216, 96%, 50%)',
            '600': 'hsl(216, 96%, 40%)',
            '700': 'hsl(216, 96%, 32%)',
            '800': 'hsl(216, 96%, 24%)',
            '900': 'hsl(216, 96%, 16%)',
            '950': 'hsl(216, 96%, 10%)',
            DEFAULT: '#4d94fb'
        },
        'neutral-50': '#000000',
        'neutral-100': '#1e2126',
        'neutral-200': '#373a40',
        'neutral-300': '#b7babf',
        'neutral-400': '#585c62',
        'neutral-500': '#82858b',
        'neutral-600': '#797979',
        'neutral-700': '#ebedef',
        'neutral-800': '#959595',
        'neutral-900': '#ffffff',
        background: '#f2f2f2',
        foreground: '#222222'
    },
    fontFamily: {
        body: [
            'Paper Mono',
            'sans-serif'
        ],
        heading: [
            'Matter',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '12px',
                letterSpacing: '0.6px'
            }
        ],
        '11': [
            '11px',
            {
                lineHeight: '16px',
                letterSpacing: '0.18px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16px',
                letterSpacing: '0.18px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '16px',
                letterSpacing: '0.18px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18px',
                letterSpacing: '0.18px'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '22px',
                letterSpacing: '0.18px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '28px',
                letterSpacing: '0.18px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '28px',
                letterSpacing: '-0.44px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '28px',
                letterSpacing: '-0.52px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '36px',
                letterSpacing: '-0.36px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px',
                letterSpacing: '-0.96px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px',
                letterSpacing: '-1.28px'
            }
        ]
    },
    spacing: {
        '14': '28px',
        '20': '40px',
        '24': '48px',
        '26': '52px',
        '30': '60px',
        '32': '64px',
        '40': '80px',
        '45': '90px',
        '48': '96px',
        '56': '112px',
        '60': '120px',
        '73': '146px',
        '77': '154px',
        '120': '240px',
        '1px': '1px'
    },
    borderRadius: {
        xs: '0px',
        sm: '4px',
        md: '8px',
        lg: '12px',
        xl: '24px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgb(215, 215, 215) 0px 0px 0px 0.75px inset',
        xs: 'rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px -1px 0px 0px inset',
        md: 'rgba(0, 0, 0, 0.08) 0px 8px 8px -4px, rgba(0, 0, 0, 0.08) 0px 2px 4px -2px, rgba(0, 0, 0, 0.08) 0px 1px 1px -1px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px',
        xl: 'rgba(0, 0, 0, 0.12) 0px 16px 32px -16px, rgba(0, 0, 0, 0.08) 0px 8px 16px -8px, rgba(0, 0, 0, 0.04) 0px 4px 8px -4px, rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px'
    },
    screens: {
        sm: '640px',
        md: '720px',
        '900px': '900px',
        '1140px': '1140px',
        '1471px': '1471px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '550': '0.55s',
        '800': '0.8s',
        '1000': '1s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.34, 1.3, 0.64, 1)',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1080px'
    }
},
  },
};
