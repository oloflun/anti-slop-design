/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(85, 100%, 97%)',
            '100': 'hsl(85, 100%, 94%)',
            '200': 'hsl(85, 100%, 86%)',
            '300': 'hsl(85, 100%, 76%)',
            '400': 'hsl(85, 100%, 64%)',
            '500': 'hsl(85, 100%, 50%)',
            '600': 'hsl(85, 100%, 40%)',
            '700': 'hsl(85, 100%, 32%)',
            '800': 'hsl(85, 100%, 24%)',
            '900': 'hsl(85, 100%, 16%)',
            '950': 'hsl(85, 100%, 10%)',
            DEFAULT: '#c0ff66'
        },
        secondary: {
            '50': 'hsl(240, 100%, 97%)',
            '100': 'hsl(240, 100%, 94%)',
            '200': 'hsl(240, 100%, 86%)',
            '300': 'hsl(240, 100%, 76%)',
            '400': 'hsl(240, 100%, 64%)',
            '500': 'hsl(240, 100%, 50%)',
            '600': 'hsl(240, 100%, 40%)',
            '700': 'hsl(240, 100%, 32%)',
            '800': 'hsl(240, 100%, 24%)',
            '900': 'hsl(240, 100%, 16%)',
            '950': 'hsl(240, 100%, 10%)',
            DEFAULT: '#0000ee'
        },
        accent: {
            '50': 'hsl(142, 71%, 97%)',
            '100': 'hsl(142, 71%, 94%)',
            '200': 'hsl(142, 71%, 86%)',
            '300': 'hsl(142, 71%, 76%)',
            '400': 'hsl(142, 71%, 64%)',
            '500': 'hsl(142, 71%, 50%)',
            '600': 'hsl(142, 71%, 40%)',
            '700': 'hsl(142, 71%, 32%)',
            '800': 'hsl(142, 71%, 24%)',
            '900': 'hsl(142, 71%, 16%)',
            '950': 'hsl(142, 71%, 10%)',
            DEFAULT: '#22c55e'
        },
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#403a35',
        'neutral-300': '#767676',
        'neutral-400': '#9e9d9b',
        'neutral-500': '#575551',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ],
        heading: [
            'Geigy LL Duplex Var Variable Reg',
            'sans-serif'
        ],
        body: [
            'ABC Arizona Flare Regular',
            'sans-serif'
        ],
        font3: [
            'Inter Variable',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '15px',
                letterSpacing: '1px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '21px',
                letterSpacing: '0.28px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '21px',
                letterSpacing: '-0.28px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '25.2px',
                letterSpacing: '-0.36px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px',
                letterSpacing: '0.28px'
            }
        ],
        '21': [
            '21px',
            {
                lineHeight: '26.25px',
                letterSpacing: '-0.63px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '31.2px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '38.4px',
                letterSpacing: '-1.12px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '52.8px',
                letterSpacing: '-2.16px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '66px',
                letterSpacing: '-1.8px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '75.6px',
                letterSpacing: '-3.6px'
            }
        ],
        '117.101': [
            '117.101px',
            {
                lineHeight: '117.101px',
                letterSpacing: '-7.02604px'
            }
        ]
    },
    spacing: {
        '12': '24px',
        '15': '30px',
        '18': '36px',
        '20': '40px',
        '23': '46px',
        '32': '64px',
        '36': '72px',
        '48': '96px',
        '60': '120px',
        '1px': '1px',
        '91px': '91px'
    },
    borderRadius: {
        xs: '1px',
        sm: '4px',
        md: '8px',
        full: '999px'
    },
    boxShadow: {
        xs: 'rgba(0, 0, 0, 0.08) 0px -1px 0px 0px, rgba(0, 0, 0, 0.06) 0px -8px 32px 0px',
        md: 'rgba(0, 0, 0, 0.12) 0px 0px 10px 0px'
    },
    screens: {
        sm: '651px',
        md: '810px'
    },
    transitionDuration: {
        '300': '0.3s',
        '500': '0.5s'
    },
    transitionTimingFunction: {
        default: 'ease',
        custom: 'cubic-bezier(0.44, 0, 0.56, 1)'
    },
    container: {
        center: true,
        padding: '40px'
    },
    maxWidth: {
        container: '1280px'
    }
},
  },
};
