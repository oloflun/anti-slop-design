/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(17, 100%, 97%)',
            '100': 'hsl(17, 100%, 94%)',
            '200': 'hsl(17, 100%, 86%)',
            '300': 'hsl(17, 100%, 76%)',
            '400': 'hsl(17, 100%, 64%)',
            '500': 'hsl(17, 100%, 50%)',
            '600': 'hsl(17, 100%, 40%)',
            '700': 'hsl(17, 100%, 32%)',
            '800': 'hsl(17, 100%, 24%)',
            '900': 'hsl(17, 100%, 16%)',
            '950': 'hsl(17, 100%, 10%)',
            DEFAULT: '#ff7f4c'
        },
        secondary: {
            '50': 'hsl(120, 100%, 97%)',
            '100': 'hsl(120, 100%, 94%)',
            '200': 'hsl(120, 100%, 86%)',
            '300': 'hsl(120, 100%, 76%)',
            '400': 'hsl(120, 100%, 64%)',
            '500': 'hsl(120, 100%, 50%)',
            '600': 'hsl(120, 100%, 40%)',
            '700': 'hsl(120, 100%, 32%)',
            '800': 'hsl(120, 100%, 24%)',
            '900': 'hsl(120, 100%, 16%)',
            '950': 'hsl(120, 100%, 10%)',
            DEFAULT: '#008000'
        },
        accent: {
            '50': 'hsl(199, 100%, 97%)',
            '100': 'hsl(199, 100%, 94%)',
            '200': 'hsl(199, 100%, 86%)',
            '300': 'hsl(199, 100%, 76%)',
            '400': 'hsl(199, 100%, 64%)',
            '500': 'hsl(199, 100%, 50%)',
            '600': 'hsl(199, 100%, 40%)',
            '700': 'hsl(199, 100%, 32%)',
            '800': 'hsl(199, 100%, 24%)',
            '900': 'hsl(199, 100%, 16%)',
            '950': 'hsl(199, 100%, 10%)',
            DEFAULT: '#0073aa'
        },
        'neutral-50': '#000000',
        'neutral-100': '#1a1819',
        'neutral-200': '#ffffff',
        'neutral-300': '#828282',
        'neutral-400': '#181d27',
        'neutral-500': '#8c8c8c',
        'neutral-600': '#ecf1f7',
        'neutral-700': '#c6c6c6',
        'neutral-800': '#334155',
        'neutral-900': '#414651',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Neue Haas Grotesk RoundDots - 55 Roman',
            'sans-serif'
        ],
        body: [
            'ETmodules',
            'sans-serif'
        ],
        font2: [
            'Helvetica',
            'sans-serif'
        ],
        heading: [
            'Neue Haas Grotesk RoundDots - 45 Light',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '21px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '24px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '28.9px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '21.6px',
                letterSpacing: '1px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '33.6px',
                letterSpacing: '0.6px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: 'normal'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '54px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '48px',
                letterSpacing: '0.6px'
            }
        ],
        '50': [
            '50px',
            {
                lineHeight: '24px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '80px'
            }
        ],
        '76.8': [
            '76.8px',
            {
                lineHeight: '76.8px',
                letterSpacing: '1.3px'
            }
        ],
        '67.2': [
            '67.2px',
            {
                lineHeight: '73.92px',
                letterSpacing: '0.6px'
            }
        ],
        '13.3333': [
            '13.3333px',
            {
                lineHeight: 'normal'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '6': '12px',
        '7': '14px',
        '10': '20px',
        '11': '22px',
        '12': '24px',
        '16': '32px',
        '18': '36px',
        '20': '40px',
        '23': '46px',
        '25': '50px',
        '39': '78px',
        '40': '80px',
        '50': '100px',
        '89': '178px',
        '29px': '29px',
        '67px': '67px',
        '83px': '83px',
        '267px': '267px'
    },
    borderRadius: {
        xs: '1px',
        sm: '4px',
        md: '8px',
        lg: '12px',
        xl: '20px',
        full: '160px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0.02) 0px 4px 4px 0px',
        xs: 'rgba(10, 13, 18, 0.05) 0px 1px 2px 0px',
        lg: 'rgba(0, 0, 0, 0.19) 0px 10px 20px 0px, rgba(0, 0, 0, 0.23) 0px 6px 6px 0px',
        xl: 'rgba(0, 0, 0, 0.2) 2px 8px 60px -2px'
    },
    screens: {
        xs: '350px',
        sm: '576px',
        lg: '992px',
        '1725px': '1725px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '200': '0.2s',
        '275': '0.275s',
        '300': '0.3s',
        '350': '0.35s',
        '400': '0.4s',
        '500': '0.5s',
        '600': '0.6s',
        '750': '0.75s',
        '1000': '1s',
        '4001.0000000000005': '4.001s'
    },
    transitionTimingFunction: {
        default: 'ease',
        linear: 'linear',
        custom: 'cubic-bezier(0.23, 1, 0.32, 1)'
    },
    container: {
        center: true,
        padding: '20px'
    },
    maxWidth: {
        container: '100%'
    }
},
  },
};
