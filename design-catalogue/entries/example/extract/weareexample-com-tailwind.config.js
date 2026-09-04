/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(195, 100%, 97%)',
            '100': 'hsl(195, 100%, 94%)',
            '200': 'hsl(195, 100%, 86%)',
            '300': 'hsl(195, 100%, 76%)',
            '400': 'hsl(195, 100%, 64%)',
            '500': 'hsl(195, 100%, 50%)',
            '600': 'hsl(195, 100%, 40%)',
            '700': 'hsl(195, 100%, 32%)',
            '800': 'hsl(195, 100%, 24%)',
            '900': 'hsl(195, 100%, 16%)',
            '950': 'hsl(195, 100%, 10%)',
            DEFAULT: '#2cc9ff'
        },
        secondary: {
            '50': 'hsl(0, 100%, 97%)',
            '100': 'hsl(0, 100%, 94%)',
            '200': 'hsl(0, 100%, 86%)',
            '300': 'hsl(0, 100%, 76%)',
            '400': 'hsl(0, 100%, 64%)',
            '500': 'hsl(0, 100%, 50%)',
            '600': 'hsl(0, 100%, 40%)',
            '700': 'hsl(0, 100%, 32%)',
            '800': 'hsl(0, 100%, 24%)',
            '900': 'hsl(0, 100%, 16%)',
            '950': 'hsl(0, 100%, 10%)',
            DEFAULT: '#ff0000'
        },
        accent: {
            '50': 'hsl(0, 100%, 97%)',
            '100': 'hsl(0, 100%, 94%)',
            '200': 'hsl(0, 100%, 86%)',
            '300': 'hsl(0, 100%, 76%)',
            '400': 'hsl(0, 100%, 64%)',
            '500': 'hsl(0, 100%, 50%)',
            '600': 'hsl(0, 100%, 40%)',
            '700': 'hsl(0, 100%, 32%)',
            '800': 'hsl(0, 100%, 24%)',
            '900': 'hsl(0, 100%, 16%)',
            '950': 'hsl(0, 100%, 10%)',
            DEFAULT: '#ffdede'
        },
        'neutral-50': '#f3f3f0',
        'neutral-100': '#000000',
        'neutral-200': '#424242',
        'neutral-300': '#1f1f1f',
        'neutral-400': '#ffffff',
        'neutral-500': '#dddddd',
        'neutral-600': '#111111',
        background: '#f3f3f0',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'American Grotesk',
            'sans-serif'
        ],
        heading: [
            'American Grotesk Compressed',
            'sans-serif'
        ],
        body: [
            'Menlo',
            'sans-serif'
        ]
    },
    fontSize: {
        '32': [
            '32px',
            {
                lineHeight: '25.6px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '51.2px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '57.6px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '79.36px',
                letterSpacing: '-0.552px'
            }
        ],
        '230.4': [
            '230.4px',
            {
                lineHeight: '179.712px',
                letterSpacing: '-0.552px'
            }
        ],
        '184.32': [
            '184.32px',
            {
                lineHeight: '147.456px'
            }
        ],
        '182.4': [
            '182.4px',
            {
                lineHeight: '145.92px'
            }
        ],
        '166.4': [
            '166.4px',
            {
                lineHeight: '133.12px'
            }
        ],
        '140.8': [
            '140.8px',
            {
                lineHeight: '112.64px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '81.92px'
            }
        ],
        '38.4': [
            '38.4px',
            {
                lineHeight: '30.72px'
            }
        ],
        '35.84': [
            '35.84px',
            {
                lineHeight: '28.672px'
            }
        ],
        '23.04': [
            '23.04px',
            {
                lineHeight: '18.432px'
            }
        ],
        '20.48': [
            '20.48px',
            {
                lineHeight: '21.504px',
                letterSpacing: '0.2048px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '22.08px',
                letterSpacing: '-0.576px'
            }
        ]
    },
    spacing: {
        '5': '10px',
        '6': '12px',
        '12': '24px',
        '16': '32px',
        '18': '36px',
        '19': '38px',
        '32': '64px',
        '40': '80px',
        '51': '102px',
        '52': '104px',
        '63': '126px',
        '64': '128px',
        '70': '140px',
        '96': '192px',
        '1px': '1px',
        '51px': '51px'
    },
    borderRadius: {
        xs: '2px',
        md: '6px'
    },
    screens: {
        md: '768px',
        '1440px': '1440px'
    },
    transitionDuration: {
        '200': '0.2s',
        '300': '0.3s'
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
