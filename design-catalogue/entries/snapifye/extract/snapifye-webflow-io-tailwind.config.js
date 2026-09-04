/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(27, 81%, 97%)',
            '100': 'hsl(27, 81%, 94%)',
            '200': 'hsl(27, 81%, 86%)',
            '300': 'hsl(27, 81%, 76%)',
            '400': 'hsl(27, 81%, 64%)',
            '500': 'hsl(27, 81%, 50%)',
            '600': 'hsl(27, 81%, 40%)',
            '700': 'hsl(27, 81%, 32%)',
            '800': 'hsl(27, 81%, 24%)',
            '900': 'hsl(27, 81%, 16%)',
            '950': 'hsl(27, 81%, 10%)',
            DEFAULT: '#f9dcc5'
        },
        secondary: {
            '50': 'hsl(359, 58%, 97%)',
            '100': 'hsl(359, 58%, 94%)',
            '200': 'hsl(359, 58%, 86%)',
            '300': 'hsl(359, 58%, 76%)',
            '400': 'hsl(359, 58%, 64%)',
            '500': 'hsl(359, 58%, 50%)',
            '600': 'hsl(359, 58%, 40%)',
            '700': 'hsl(359, 58%, 32%)',
            '800': 'hsl(359, 58%, 24%)',
            '900': 'hsl(359, 58%, 16%)',
            '950': 'hsl(359, 58%, 10%)',
            DEFAULT: '#701e1f'
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
            DEFAULT: '#ff2f2f'
        },
        'neutral-50': '#ffffff',
        'neutral-100': '#000000',
        'neutral-200': '#161616',
        'neutral-300': '#474747',
        'neutral-400': '#222222',
        background: '#f9dcc5',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Gt Walsheim Trial',
            'sans-serif'
        ],
        body: [
            'PT Sans',
            'sans-serif'
        ]
    },
    fontSize: {
        '14': [
            '14px',
            {
                lineHeight: '14px'
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
                lineHeight: '18px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '20px'
            }
        ],
        '24': [
            '24px',
            {
                lineHeight: '24px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px'
            }
        ],
        '184': [
            '184px',
            {
                lineHeight: '147.2px',
                letterSpacing: '-0.8px'
            }
        ],
        '158.113': [
            '158.113px',
            {
                lineHeight: '158.113px'
            }
        ],
        '133.334': [
            '133.334px',
            {
                lineHeight: '106.667px'
            }
        ],
        '113.208': [
            '113.208px',
            {
                lineHeight: '90.5664px'
            }
        ],
        '66.792': [
            '66.792px',
            {
                lineHeight: '58.109px'
            }
        ],
        '47.5462': [
            '47.5462px',
            {
                lineHeight: '47.5462px'
            }
        ],
        '46.5875': [
            '46.5875px',
            {
                lineHeight: '51.2463px'
            }
        ],
        '23.4336': [
            '23.4336px',
            {
                lineHeight: '23.4336px'
            }
        ],
        '23.2458': [
            '23.2458px',
            {
                lineHeight: '23.2458px'
            }
        ]
    },
    spacing: {
        '8': '40px',
        '12': '60px',
        '16': '80px',
        '20': '100px',
        '23': '115px',
        '24': '120px',
        '28': '140px',
        '35': '175px',
        '36': '180px',
        '53': '265px',
        '84': '420px',
        '88': '440px',
        '1px': '1px',
        '203px': '203px'
    },
    borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '16px',
        xl: '24px',
        full: '99px'
    },
    screens: {
        md: '768px',
        lg: '992px',
        xl: '1280px',
        '1440px': '1440px',
        '1920px': '1920px'
    },
    transitionDuration: {
        '100': '0.1s',
        '250': '0.25s',
        '300': '0.3s',
        '350': '0.35s'
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
