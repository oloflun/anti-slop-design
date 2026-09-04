/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(166, 39%, 97%)',
            '100': 'hsl(166, 39%, 94%)',
            '200': 'hsl(166, 39%, 86%)',
            '300': 'hsl(166, 39%, 76%)',
            '400': 'hsl(166, 39%, 64%)',
            '500': 'hsl(166, 39%, 50%)',
            '600': 'hsl(166, 39%, 40%)',
            '700': 'hsl(166, 39%, 32%)',
            '800': 'hsl(166, 39%, 24%)',
            '900': 'hsl(166, 39%, 16%)',
            '950': 'hsl(166, 39%, 10%)',
            DEFAULT: '#0a1714'
        },
        secondary: {
            '50': 'hsl(36, 100%, 97%)',
            '100': 'hsl(36, 100%, 94%)',
            '200': 'hsl(36, 100%, 86%)',
            '300': 'hsl(36, 100%, 76%)',
            '400': 'hsl(36, 100%, 64%)',
            '500': 'hsl(36, 100%, 50%)',
            '600': 'hsl(36, 100%, 40%)',
            '700': 'hsl(36, 100%, 32%)',
            '800': 'hsl(36, 100%, 24%)',
            '900': 'hsl(36, 100%, 16%)',
            '950': 'hsl(36, 100%, 10%)',
            DEFAULT: '#fff7eb'
        },
        accent: {
            '50': 'hsl(54, 100%, 97%)',
            '100': 'hsl(54, 100%, 94%)',
            '200': 'hsl(54, 100%, 86%)',
            '300': 'hsl(54, 100%, 76%)',
            '400': 'hsl(54, 100%, 64%)',
            '500': 'hsl(54, 100%, 50%)',
            '600': 'hsl(54, 100%, 40%)',
            '700': 'hsl(54, 100%, 32%)',
            '800': 'hsl(54, 100%, 24%)',
            '900': 'hsl(54, 100%, 16%)',
            '950': 'hsl(54, 100%, 10%)',
            DEFAULT: '#fff8bb'
        },
        'neutral-50': '#000000',
        'neutral-100': '#61805b',
        'neutral-200': '#ffffff',
        'neutral-300': '#767676',
        'neutral-400': '#bbd0b7',
        background: '#efe5d4',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ],
        heading: [
            'SeriouslyNostalgic Condensed',
            'sans-serif'
        ],
        body: [
            'Times New Roman',
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
        '13': [
            '13px',
            {
                lineHeight: '20px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '12px',
                letterSpacing: '1.25px'
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
                lineHeight: '28px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px',
                letterSpacing: '-0.25px'
            }
        ],
        '32': [
            '32px',
            {
                lineHeight: '32px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px',
                letterSpacing: '1px'
            }
        ],
        '64': [
            '64px',
            {
                lineHeight: '64px',
                letterSpacing: '1px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '56px'
            }
        ],
        '88': [
            '88px',
            {
                lineHeight: '84px',
                letterSpacing: '2px'
            }
        ],
        '96': [
            '96px',
            {
                lineHeight: '80px'
            }
        ],
        '128': [
            '128px',
            {
                lineHeight: '104px'
            }
        ]
    },
    spacing: {
        '8': '32px',
        '12': '48px',
        '20': '80px',
        '30': '120px',
        '40': '160px',
        '50': '200px',
        '1px': '1px',
        '37px': '37px',
        '53px': '53px',
        '61px': '61px'
    },
    borderRadius: {
        lg: '16px',
        xl: '24px',
        full: '100px'
    },
    screens: {
        md: '810px',
        lg: '1024px'
    },
    transitionDuration: {
        '400': '0.4s'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '1440px'
    }
},
  },
};
