/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(48, 38%, 97%)',
            '100': 'hsl(48, 38%, 94%)',
            '200': 'hsl(48, 38%, 86%)',
            '300': 'hsl(48, 38%, 76%)',
            '400': 'hsl(48, 38%, 64%)',
            '500': 'hsl(48, 38%, 50%)',
            '600': 'hsl(48, 38%, 40%)',
            '700': 'hsl(48, 38%, 32%)',
            '800': 'hsl(48, 38%, 24%)',
            '900': 'hsl(48, 38%, 16%)',
            '950': 'hsl(48, 38%, 10%)',
            DEFAULT: '#fbfaf6'
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
            '50': 'hsl(0, 92%, 97%)',
            '100': 'hsl(0, 92%, 94%)',
            '200': 'hsl(0, 92%, 86%)',
            '300': 'hsl(0, 92%, 76%)',
            '400': 'hsl(0, 92%, 64%)',
            '500': 'hsl(0, 92%, 50%)',
            '600': 'hsl(0, 92%, 40%)',
            '700': 'hsl(0, 92%, 32%)',
            '800': 'hsl(0, 92%, 24%)',
            '900': 'hsl(0, 92%, 16%)',
            '950': 'hsl(0, 92%, 10%)',
            DEFAULT: '#f50c0c'
        },
        'neutral-50': '#000000',
        'neutral-100': '#2b2b29',
        'neutral-200': '#a5beba',
        'neutral-300': '#494444',
        'neutral-400': '#918f66',
        'neutral-500': '#918989',
        'neutral-600': '#c8bcae',
        'neutral-700': '#e4e2d9',
        'neutral-800': '#83a5a0',
        background: '#fbfaf6',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'GT Standard L Medium',
            'sans-serif'
        ],
        heading: [
            'Source Serif 4 Variable',
            'sans-serif'
        ]
    },
    fontSize: {
        '32': [
            '32px',
            {
                lineHeight: '32px',
                letterSpacing: '-1.6px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '44px',
                letterSpacing: '-1.76px'
            }
        ],
        '56': [
            '56px',
            {
                lineHeight: '56px',
                letterSpacing: '-2.24px'
            }
        ],
        '62': [
            '62px',
            {
                lineHeight: '62px',
                letterSpacing: '-2.48px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px',
                letterSpacing: '-2.56px'
            }
        ],
        '268': [
            '268px',
            {
                lineHeight: '241.2px',
                letterSpacing: '-13.4px'
            }
        ],
        '597.662': [
            '597.662px',
            {
                lineHeight: '597.662px',
                letterSpacing: '-23.9065px'
            }
        ],
        '354.9': [
            '354.9px',
            {
                lineHeight: '319.41px',
                letterSpacing: '-17.745px'
            }
        ],
        '328.936': [
            '328.936px',
            {
                lineHeight: '328.936px',
                letterSpacing: '-13.1574px'
            }
        ],
        '316.339': [
            '316.339px',
            {
                lineHeight: '316.339px',
                letterSpacing: '-12.6535px'
            }
        ],
        '311.21': [
            '311.21px',
            {
                lineHeight: '311.21px',
                letterSpacing: '-12.4484px'
            }
        ],
        '228.851': [
            '228.851px',
            {
                lineHeight: '205.966px',
                letterSpacing: '-11.4426px'
            }
        ],
        '135.252': [
            '135.252px',
            {
                lineHeight: '121.726px',
                letterSpacing: '-6.76258px'
            }
        ],
        '42.6667': [
            '42.6667px',
            {
                lineHeight: '42.6667px'
            }
        ],
        '29.3333': [
            '29.3333px',
            {
                lineHeight: '29.3333px'
            }
        ]
    },
    spacing: {
        '15': '30px',
        '20': '40px',
        '24': '48px',
        '30': '60px',
        '37': '74px',
        '40': '80px',
        '50': '100px',
        '60': '120px',
        '80': '160px',
        '92': '184px',
        '100': '200px',
        '1px': '1px'
    },
    borderRadius: {
        md: '8px',
        xl: '24px',
        full: '10000px'
    },
    screens: {
        md: '810px',
        '1200px': '1200px'
    },
    transitionDuration: {
        '1': '0.001s',
        '320': '0.32s',
        '350': '0.35s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.22, 1, 0.36, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '600px'
    }
},
  },
};
