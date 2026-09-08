/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(2, 87%, 97%)',
            '100': 'hsl(2, 87%, 94%)',
            '200': 'hsl(2, 87%, 86%)',
            '300': 'hsl(2, 87%, 76%)',
            '400': 'hsl(2, 87%, 64%)',
            '500': 'hsl(2, 87%, 50%)',
            '600': 'hsl(2, 87%, 40%)',
            '700': 'hsl(2, 87%, 32%)',
            '800': 'hsl(2, 87%, 24%)',
            '900': 'hsl(2, 87%, 16%)',
            '950': 'hsl(2, 87%, 10%)',
            DEFAULT: '#3b0604'
        },
        secondary: {
            '50': 'hsl(3, 76%, 97%)',
            '100': 'hsl(3, 76%, 94%)',
            '200': 'hsl(3, 76%, 86%)',
            '300': 'hsl(3, 76%, 76%)',
            '400': 'hsl(3, 76%, 64%)',
            '500': 'hsl(3, 76%, 50%)',
            '600': 'hsl(3, 76%, 40%)',
            '700': 'hsl(3, 76%, 32%)',
            '800': 'hsl(3, 76%, 24%)',
            '900': 'hsl(3, 76%, 16%)',
            '950': 'hsl(3, 76%, 10%)',
            DEFAULT: '#751510'
        },
        accent: {
            '50': 'hsl(45, 42%, 97%)',
            '100': 'hsl(45, 42%, 94%)',
            '200': 'hsl(45, 42%, 86%)',
            '300': 'hsl(45, 42%, 76%)',
            '400': 'hsl(45, 42%, 64%)',
            '500': 'hsl(45, 42%, 50%)',
            '600': 'hsl(45, 42%, 40%)',
            '700': 'hsl(45, 42%, 32%)',
            '800': 'hsl(45, 42%, 24%)',
            '900': 'hsl(45, 42%, 16%)',
            '950': 'hsl(45, 42%, 10%)',
            DEFAULT: '#e7dec4'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#040201',
        'neutral-200': '#1c1611',
        background: '#e7dec4',
        foreground: '#040201'
    },
    fontFamily: {
        body: [
            'IBM Plex Mono',
            'sans-serif'
        ],
        font2: [
            'Cormorant Garamond',
            'sans-serif'
        ]
    },
    fontSize: {
        '16': [
            '16px',
            {
                lineHeight: '24px'
            }
        ],
        '17': [
            '17px',
            {
                lineHeight: '26.35px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px',
                letterSpacing: '-0.3px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '32px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '36px',
                letterSpacing: '-0.45px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '40px',
                letterSpacing: '-0.9px'
            }
        ],
        '153.6': [
            '153.6px',
            {
                lineHeight: '147.456px',
                letterSpacing: '-2.304px'
            }
        ],
        '121.6': [
            '121.6px',
            {
                lineHeight: '114.304px',
                letterSpacing: '-1.824px'
            }
        ],
        '89.6': [
            '89.6px',
            {
                lineHeight: '85.12px',
                letterSpacing: '-1.344px'
            }
        ],
        '70.4': [
            '70.4px',
            {
                lineHeight: '68.992px',
                letterSpacing: '-1.056px'
            }
        ],
        '53.76': [
            '53.76px',
            {
                lineHeight: '58.0608px',
                letterSpacing: '-0.8064px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '53.76px',
                letterSpacing: '-0.768px'
            }
        ],
        '43.52': [
            '43.52px',
            {
                lineHeight: '48.7424px',
                letterSpacing: '-0.6528px'
            }
        ],
        '17.5': [
            '17.5px',
            {
                lineHeight: '26.25px'
            }
        ],
        '16.5': [
            '16.5px',
            {
                lineHeight: '27.225px'
            }
        ]
    },
    spacing: {
        '1': '4px',
        '10': '40px',
        '12': '48px',
        '14': '56px',
        '16': '64px',
        '20': '80px',
        '24': '96px',
        '32': '128px'
    },
    screens: {
        sm: '640px',
        md: '768px'
    },
    transitionDuration: {
        '1250': '1.25s',
        '1400': '1.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)'
    },
    container: {
        center: true,
        padding: '32px'
    },
    maxWidth: {
        container: '1480px'
    }
},
  },
};
