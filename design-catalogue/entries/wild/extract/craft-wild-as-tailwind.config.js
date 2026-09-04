/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(69, 100%, 97%)',
            '100': 'hsl(69, 100%, 94%)',
            '200': 'hsl(69, 100%, 86%)',
            '300': 'hsl(69, 100%, 76%)',
            '400': 'hsl(69, 100%, 64%)',
            '500': 'hsl(69, 100%, 50%)',
            '600': 'hsl(69, 100%, 40%)',
            '700': 'hsl(69, 100%, 32%)',
            '800': 'hsl(69, 100%, 24%)',
            '900': 'hsl(69, 100%, 16%)',
            '950': 'hsl(69, 100%, 10%)',
            DEFAULT: '#d8ff00'
        },
        secondary: {
            '50': 'hsl(47, 92%, 97%)',
            '100': 'hsl(47, 92%, 94%)',
            '200': 'hsl(47, 92%, 86%)',
            '300': 'hsl(47, 92%, 76%)',
            '400': 'hsl(47, 92%, 64%)',
            '500': 'hsl(47, 92%, 50%)',
            '600': 'hsl(47, 92%, 40%)',
            '700': 'hsl(47, 92%, 32%)',
            '800': 'hsl(47, 92%, 24%)',
            '900': 'hsl(47, 92%, 16%)',
            '950': 'hsl(47, 92%, 10%)',
            DEFAULT: '#f5c518'
        },
        accent: {
            '50': 'hsl(252, 85%, 97%)',
            '100': 'hsl(252, 85%, 94%)',
            '200': 'hsl(252, 85%, 86%)',
            '300': 'hsl(252, 85%, 76%)',
            '400': 'hsl(252, 85%, 64%)',
            '500': 'hsl(252, 85%, 50%)',
            '600': 'hsl(252, 85%, 40%)',
            '700': 'hsl(252, 85%, 32%)',
            '800': 'hsl(252, 85%, 24%)',
            '900': 'hsl(252, 85%, 16%)',
            '950': 'hsl(252, 85%, 10%)',
            DEFAULT: '#6c4cf1'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#0a0a0a',
        'neutral-200': '#2a2a2a',
        'neutral-300': '#000000',
        'neutral-400': '#8b8b8b',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Sneak',
            'sans-serif'
        ],
        heading: [
            'Arial',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ]
    },
    fontSize: {
        '11': [
            '11px',
            {
                lineHeight: '16.5px',
                letterSpacing: '1.43px'
            }
        ],
        '13': [
            '13px',
            {
                lineHeight: '18.85px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '22.68px'
            }
        ],
        '15': [
            '15px',
            {
                lineHeight: '24.3px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '33px',
                letterSpacing: '1.76px'
            }
        ],
        '34': [
            '34px',
            {
                lineHeight: '34px',
                letterSpacing: '-0.68px'
            }
        ],
        '66.56': [
            '66.56px',
            {
                lineHeight: '61.2352px',
                letterSpacing: '-2.3296px'
            }
        ],
        '43.52': [
            '43.52px',
            {
                lineHeight: '46.1312px',
                letterSpacing: '-0.8704px'
            }
        ],
        '28.16': [
            '28.16px',
            {
                lineHeight: '42.24px',
                letterSpacing: '-0.5632px'
            }
        ],
        '18.56': [
            '18.56px',
            {
                lineHeight: '21.9008px',
                letterSpacing: '-0.1856px'
            }
        ],
        '15.36': [
            '15.36px',
            {
                lineHeight: '23.04px',
                letterSpacing: '-0.1536px'
            }
        ],
        '14.5': [
            '14.5px',
            {
                lineHeight: '21.75px'
            }
        ],
        '13.5': [
            '13.5px',
            {
                lineHeight: '20.25px'
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
        '6': '12px',
        '13': '26px',
        '21': '42px',
        '28': '56px',
        '49': '98px',
        '63': '126px',
        '84': '168px',
        '178': '356px',
        '1px': '1px',
        '35px': '35px',
        '49px': '49px'
    },
    borderRadius: {
        md: '10px'
    },
    boxShadow: {
        md: 'rgba(10, 10, 10, 0.14) 0px 2px 12px 0px'
    },
    screens: {
        '560px': '560px',
        '840px': '840px',
        '860px': '860px',
        '880px': '880px',
        '900px': '900px'
    },
    transitionDuration: {
        '100': '0.1s',
        '120': '0.12s',
        '150': '0.15s',
        '200': '0.2s',
        '240': '0.24s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s',
        '360': '0.36s',
        '400': '0.4s',
        '450': '0.45s',
        '500': '0.5s',
        '550': '0.55s',
        '800': '0.8s',
        '850': '0.85s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1176px'
    }
},
  },
};
