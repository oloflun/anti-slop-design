/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(14, 100%, 97%)',
            '100': 'hsl(14, 100%, 94%)',
            '200': 'hsl(14, 100%, 86%)',
            '300': 'hsl(14, 100%, 76%)',
            '400': 'hsl(14, 100%, 64%)',
            '500': 'hsl(14, 100%, 50%)',
            '600': 'hsl(14, 100%, 40%)',
            '700': 'hsl(14, 100%, 32%)',
            '800': 'hsl(14, 100%, 24%)',
            '900': 'hsl(14, 100%, 16%)',
            '950': 'hsl(14, 100%, 10%)',
            DEFAULT: '#ff531f'
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
            '50': 'hsl(14, 100%, 97%)',
            '100': 'hsl(14, 100%, 94%)',
            '200': 'hsl(14, 100%, 86%)',
            '300': 'hsl(14, 100%, 76%)',
            '400': 'hsl(14, 100%, 64%)',
            '500': 'hsl(14, 100%, 50%)',
            '600': 'hsl(14, 100%, 40%)',
            '700': 'hsl(14, 100%, 32%)',
            '800': 'hsl(14, 100%, 24%)',
            '900': 'hsl(14, 100%, 16%)',
            '950': 'hsl(14, 100%, 10%)',
            DEFAULT: '#ff825c'
        },
        'neutral-50': '#000000',
        'neutral-100': '#171717',
        'neutral-200': '#ffffff',
        'neutral-300': '#767f7a',
        'neutral-400': '#dddfde',
        'neutral-500': '#f5f5f5',
        'neutral-600': '#afb6b4',
        'neutral-700': '#434645',
        'neutral-800': '#fff0eb',
        background: '#1e1f1f',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Apfel Grotezk',
            'sans-serif'
        ],
        heading: [
            'Oswald',
            'sans-serif'
        ],
        body: [
            'Instrument Sans',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '19.8px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '30px'
            }
        ],
        '21': [
            '21px',
            {
                lineHeight: '25.2px',
                letterSpacing: '-0.21px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '24px',
                letterSpacing: '-0.24px'
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
                lineHeight: '43.2px',
                letterSpacing: '-1.44px'
            }
        ],
        '98': [
            '98px',
            {
                lineHeight: '88.2px',
                letterSpacing: '-2.94px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '95px',
                letterSpacing: '-1px'
            }
        ],
        '120': [
            '120px',
            {
                lineHeight: '102px',
                letterSpacing: '-2.4px'
            }
        ],
        '152': [
            '152px',
            {
                lineHeight: '228px',
                letterSpacing: '-4.56px'
            }
        ],
        '190': [
            '190px',
            {
                lineHeight: '148.2px',
                letterSpacing: '-5.7px'
            }
        ],
        '320': [
            '320px',
            {
                lineHeight: '320px',
                letterSpacing: '-19.2px'
            }
        ],
        '104.117': [
            '104.117px',
            {
                lineHeight: '99.9525px',
                letterSpacing: '-4.16469px'
            }
        ],
        '64.855': [
            '64.855px',
            {
                lineHeight: '62.2608px',
                letterSpacing: '-2.5942px'
            }
        ]
    },
    spacing: {
        '40': '80px',
        '50': '100px',
        '60': '120px',
        '70': '140px',
        '75': '150px',
        '100': '200px',
        '1px': '1px'
    },
    borderRadius: {
        md: '10px',
        lg: '16px',
        xl: '24px',
        full: '100px'
    },
    boxShadow: {
        sm: 'rgb(0, 0, 0) 0px 0px 0px 1px inset',
        xs: 'rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px'
    },
    screens: {
        md: '810px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.44, 0, 0.56, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1580px'
    }
},
  },
};
