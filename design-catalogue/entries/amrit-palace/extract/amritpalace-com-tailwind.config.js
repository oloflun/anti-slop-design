/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(31, 60%, 97%)',
            '100': 'hsl(31, 60%, 94%)',
            '200': 'hsl(31, 60%, 86%)',
            '300': 'hsl(31, 60%, 76%)',
            '400': 'hsl(31, 60%, 64%)',
            '500': 'hsl(31, 60%, 50%)',
            '600': 'hsl(31, 60%, 40%)',
            '700': 'hsl(31, 60%, 32%)',
            '800': 'hsl(31, 60%, 24%)',
            '900': 'hsl(31, 60%, 16%)',
            '950': 'hsl(31, 60%, 10%)',
            DEFAULT: '#d49653'
        },
        secondary: {
            '50': 'hsl(36, 29%, 97%)',
            '100': 'hsl(36, 29%, 94%)',
            '200': 'hsl(36, 29%, 86%)',
            '300': 'hsl(36, 29%, 76%)',
            '400': 'hsl(36, 29%, 64%)',
            '500': 'hsl(36, 29%, 50%)',
            '600': 'hsl(36, 29%, 40%)',
            '700': 'hsl(36, 29%, 32%)',
            '800': 'hsl(36, 29%, 24%)',
            '900': 'hsl(36, 29%, 16%)',
            '950': 'hsl(36, 29%, 10%)',
            DEFAULT: '#d8cbb8'
        },
        'neutral-50': '#2c2c2c',
        'neutral-100': '#000000',
        'neutral-200': '#dfdad5',
        'neutral-300': '#222222',
        'neutral-400': '#efefef',
        'neutral-500': '#bfb4a3',
        background: '#d8cbb8',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'webflow-icons',
            'sans-serif'
        ],
        heading: [
            'TT Ramillas Variable',
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
        '176.64': [
            '176.64px',
            {
                lineHeight: '141.312px',
                letterSpacing: '-2.82624px'
            }
        ],
        '102.4': [
            '102.4px',
            {
                lineHeight: '81.92px',
                letterSpacing: '-4.096px'
            }
        ],
        '61.44': [
            '61.44px',
            {
                lineHeight: '49.152px',
                letterSpacing: '-2.4576px'
            }
        ],
        '57.6': [
            '57.6px',
            {
                lineHeight: '48.96px',
                letterSpacing: '-2.304px'
            }
        ],
        '44.8': [
            '44.8px',
            {
                lineHeight: '40.32px',
                letterSpacing: '-1.344px'
            }
        ],
        '37.12': [
            '37.12px',
            {
                lineHeight: '37.12px',
                letterSpacing: '-1.4848px'
            }
        ],
        '23.04': [
            '23.04px',
            {
                lineHeight: '27.648px',
                letterSpacing: '-0.128px'
            }
        ],
        '19.2': [
            '19.2px',
            {
                lineHeight: '19.2px',
                letterSpacing: '-0.672px'
            }
        ],
        '13.44': [
            '13.44px',
            {
                lineHeight: '13.44px',
                letterSpacing: '-0.128px'
            }
        ],
        '12.8': [
            '12.8px',
            {
                lineHeight: '12.8px',
                letterSpacing: '-0.128px'
            }
        ],
        '12.096': [
            '12.096px',
            {
                lineHeight: '16.9344px',
                letterSpacing: '-0.128px'
            }
        ],
        '11.52': [
            '11.52px',
            {
                lineHeight: '16.128px',
                letterSpacing: '-0.128px'
            }
        ],
        '10.88': [
            '10.88px',
            {
                lineHeight: '10.88px',
                letterSpacing: '-0.128px'
            }
        ],
        '10.24': [
            '10.24px',
            {
                lineHeight: '10.24px',
                letterSpacing: '-0.128px'
            }
        ]
    },
    spacing: {
        '20': '40px',
        '26': '52px',
        '31': '62px',
        '39': '78px',
        '45': '90px',
        '64': '128px',
        '87': '174px',
        '101': '202px',
        '116': '232px',
        '125': '250px',
        '140': '280px',
        '160': '320px',
        '1px': '1px',
        '147px': '147px',
        '245px': '245px',
        '275px': '275px'
    },
    borderRadius: {
        xs: '2px'
    },
    screens: {
        sm: '480px',
        md: '768px',
        lg: '1024px'
    },
    transitionDuration: {
        '350': '0.35s',
        '400': '0.4s',
        '450': '0.45s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
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
