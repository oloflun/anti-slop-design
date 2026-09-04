/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(196, 100%, 97%)',
            '100': 'hsl(196, 100%, 94%)',
            '200': 'hsl(196, 100%, 86%)',
            '300': 'hsl(196, 100%, 76%)',
            '400': 'hsl(196, 100%, 64%)',
            '500': 'hsl(196, 100%, 50%)',
            '600': 'hsl(196, 100%, 40%)',
            '700': 'hsl(196, 100%, 32%)',
            '800': 'hsl(196, 100%, 24%)',
            '900': 'hsl(196, 100%, 16%)',
            '950': 'hsl(196, 100%, 10%)',
            DEFAULT: '#000e13'
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
            DEFAULT: '#ffdead'
        },
        accent: {
            '50': 'hsl(40, 32%, 97%)',
            '100': 'hsl(40, 32%, 94%)',
            '200': 'hsl(40, 32%, 86%)',
            '300': 'hsl(40, 32%, 76%)',
            '400': 'hsl(40, 32%, 64%)',
            '500': 'hsl(40, 32%, 50%)',
            '600': 'hsl(40, 32%, 40%)',
            '700': 'hsl(40, 32%, 32%)',
            '800': 'hsl(40, 32%, 24%)',
            '900': 'hsl(40, 32%, 16%)',
            '950': 'hsl(40, 32%, 10%)',
            DEFAULT: '#e6dece'
        },
        'neutral-50': '#232323',
        'neutral-100': '#999999',
        'neutral-200': '#000000',
        'neutral-300': '#808080',
        background: '#e8ded0',
        foreground: '#232323'
    },
    fontFamily: {
        body: [
            'GT Pressura Mono',
            'sans-serif'
        ],
        heading: [
            'GTSectraDisplay',
            'sans-serif'
        ],
        font2: [
            'Voyage',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '14px',
                letterSpacing: '1px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16.8px',
                letterSpacing: '1px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '19.6px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '22.4px'
            }
        ],
        '26': [
            '26px',
            {
                lineHeight: '31.2px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '41.4px'
            }
        ],
        '72': [
            '72px',
            {
                lineHeight: '64.8px'
            }
        ],
        '80': [
            '80px',
            {
                lineHeight: '112px'
            }
        ],
        '90': [
            '90px',
            {
                lineHeight: '126px'
            }
        ],
        '100': [
            '100px',
            {
                lineHeight: '140px'
            }
        ],
        '110': [
            '110px',
            {
                lineHeight: '154px'
            }
        ],
        '130': [
            '130px',
            {
                lineHeight: '120px'
            }
        ],
        '180': [
            '180px',
            {
                lineHeight: '170px'
            }
        ]
    },
    spacing: {
        '1': '5px',
        '6': '30px',
        '8': '40px',
        '12': '60px',
        '18': '90px',
        '28': '140px',
        '48': '240px'
    },
    screens: {
        md: '768px',
        lg: '992px',
        '1200px': '1200px',
        xl: '1280px'
    },
    transitionDuration: {
        '200': '0.2s',
        '600': '0.6s',
        '1000': '1s',
        '1200': '1.2s',
        '1600': '1.6s',
        '2000': '2s',
        '2250': '2.25s',
        '2750': '2.75s',
        '3000': '3s',
        '4000': '4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.82, 0, 0.36, 1)'
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
