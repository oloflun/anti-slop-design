/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(16, 52%, 97%)',
            '100': 'hsl(16, 52%, 94%)',
            '200': 'hsl(16, 52%, 86%)',
            '300': 'hsl(16, 52%, 76%)',
            '400': 'hsl(16, 52%, 64%)',
            '500': 'hsl(16, 52%, 50%)',
            '600': 'hsl(16, 52%, 40%)',
            '700': 'hsl(16, 52%, 32%)',
            '800': 'hsl(16, 52%, 24%)',
            '900': 'hsl(16, 52%, 16%)',
            '950': 'hsl(16, 52%, 10%)',
            DEFAULT: '#a85435'
        },
        secondary: {
            '50': 'hsl(56, 62%, 97%)',
            '100': 'hsl(56, 62%, 94%)',
            '200': 'hsl(56, 62%, 86%)',
            '300': 'hsl(56, 62%, 76%)',
            '400': 'hsl(56, 62%, 64%)',
            '500': 'hsl(56, 62%, 50%)',
            '600': 'hsl(56, 62%, 40%)',
            '700': 'hsl(56, 62%, 32%)',
            '800': 'hsl(56, 62%, 24%)',
            '900': 'hsl(56, 62%, 16%)',
            '950': 'hsl(56, 62%, 10%)',
            DEFAULT: '#555114'
        },
        accent: {
            '50': 'hsl(35, 43%, 97%)',
            '100': 'hsl(35, 43%, 94%)',
            '200': 'hsl(35, 43%, 86%)',
            '300': 'hsl(35, 43%, 76%)',
            '400': 'hsl(35, 43%, 64%)',
            '500': 'hsl(35, 43%, 50%)',
            '600': 'hsl(35, 43%, 40%)',
            '700': 'hsl(35, 43%, 32%)',
            '800': 'hsl(35, 43%, 24%)',
            '900': 'hsl(35, 43%, 16%)',
            '950': 'hsl(35, 43%, 10%)',
            DEFAULT: '#efe5d7'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#000000',
        'neutral-200': '#ffffff',
        'neutral-300': '#6b7280',
        background: '#efe5d7',
        foreground: '#000000'
    },
    fontFamily: {
        sans: [
            'Sackers Gothic Std Heavy',
            'sans-serif'
        ],
        heading: [
            'EngraversMTPro',
            'sans-serif'
        ],
        font2: [
            'Francesco-Regular',
            'sans-serif'
        ],
        font3: [
            'Ceraph-Italic',
            'sans-serif'
        ],
        body: [
            'GTStandard-M',
            'sans-serif'
        ]
    },
    fontSize: {
        '10': [
            '10px',
            {
                lineHeight: '16px',
                letterSpacing: '1.2px'
            }
        ],
        '11': [
            '11px',
            {
                lineHeight: '16px'
            }
        ],
        '12': [
            '12px',
            {
                lineHeight: '16px',
                letterSpacing: '2.64px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '20px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: '18.4px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '23px'
            }
        ],
        '22': [
            '22px',
            {
                lineHeight: '24px'
            }
        ],
        '28': [
            '28px',
            {
                lineHeight: '32px'
            }
        ],
        '40': [
            '40px',
            {
                lineHeight: '18px',
                letterSpacing: '-3.6px'
            }
        ],
        '46': [
            '46px',
            {
                lineHeight: '54px'
            }
        ]
    },
    spacing: {
        '14': '56px',
        '18': '72px',
        '20': '80px',
        '30': '120px',
        '36': '144px',
        '38': '152px',
        '81': '324px',
        '90': '360px',
        '1px': '1px',
        '105px': '105px',
        '111px': '111px',
        '177px': '177px',
        '399px': '399px'
    },
    borderRadius: {
        xs: '2px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px',
        md: 'rgba(63, 63, 68, 0.4) 0px 4px 10px 0px'
    },
    screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        '1400px': '1400px',
        '1680px': '1680px',
        '1900px': '1900px',
        '2600px': '2600px'
    },
    transitionDuration: {
        '100': '0.1s',
        '150': '0.15s',
        '300': '0.3s',
        '400': '0.4s',
        '500': '0.5s',
        '700': '0.7s',
        '800': '0.8s',
        '875': '0.875s',
        '900': '0.9s',
        '950': '0.95s',
        '1000': '1s',
        '1025': '1.025s',
        '1050': '1.05s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.76, 0, 0.24, 1)',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '24px'
    },
    maxWidth: {
        container: '650px'
    }
},
  },
};
