/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
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
        'neutral-50': '#000000',
        'neutral-100': '#ffffff',
        'neutral-200': '#151515',
        'neutral-300': '#737373',
        'neutral-400': '#eeedec',
        'neutral-500': '#383838',
        'neutral-600': '#444444',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
            'sans-serif'
        ],
        font2: [
            'ABC Arizona Mix Regular',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: 'normal'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '21px',
                letterSpacing: '-0.14px'
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
                lineHeight: '27px',
                letterSpacing: '-0.1px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '25px',
                letterSpacing: '-0.4px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '26.4px',
                letterSpacing: '-0.48px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '35px',
                letterSpacing: '-0.84px'
            }
        ],
        '44': [
            '44px',
            {
                lineHeight: '46.2px',
                letterSpacing: '-2.2px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '50.4px',
                letterSpacing: '-2.4px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '60.8px',
                letterSpacing: '-3.2px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '128px',
                letterSpacing: '-3.84px'
            }
        ]
    },
    spacing: {
        '27': '108px',
        '30': '120px',
        '41': '164px',
        '49': '196px',
        '1px': '1px'
    },
    borderRadius: {
        md: '6px'
    },
    screens: {
        md: '810px',
        '2xl': '1600px'
    },
    transitionDuration: {
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
        container: '1280px'
    }
},
  },
};
