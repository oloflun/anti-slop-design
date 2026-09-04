/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(207, 72%, 97%)',
            '100': 'hsl(207, 72%, 94%)',
            '200': 'hsl(207, 72%, 86%)',
            '300': 'hsl(207, 72%, 76%)',
            '400': 'hsl(207, 72%, 64%)',
            '500': 'hsl(207, 72%, 50%)',
            '600': 'hsl(207, 72%, 40%)',
            '700': 'hsl(207, 72%, 32%)',
            '800': 'hsl(207, 72%, 24%)',
            '900': 'hsl(207, 72%, 16%)',
            '950': 'hsl(207, 72%, 10%)',
            DEFAULT: '#114167'
        },
        secondary: {
            '50': 'hsl(177, 100%, 97%)',
            '100': 'hsl(177, 100%, 94%)',
            '200': 'hsl(177, 100%, 86%)',
            '300': 'hsl(177, 100%, 76%)',
            '400': 'hsl(177, 100%, 64%)',
            '500': 'hsl(177, 100%, 50%)',
            '600': 'hsl(177, 100%, 40%)',
            '700': 'hsl(177, 100%, 32%)',
            '800': 'hsl(177, 100%, 24%)',
            '900': 'hsl(177, 100%, 16%)',
            '950': 'hsl(177, 100%, 10%)',
            DEFAULT: '#00f2e5'
        },
        accent: {
            '50': 'hsl(202, 57%, 97%)',
            '100': 'hsl(202, 57%, 94%)',
            '200': 'hsl(202, 57%, 86%)',
            '300': 'hsl(202, 57%, 76%)',
            '400': 'hsl(202, 57%, 64%)',
            '500': 'hsl(202, 57%, 50%)',
            '600': 'hsl(202, 57%, 40%)',
            '700': 'hsl(202, 57%, 32%)',
            '800': 'hsl(202, 57%, 24%)',
            '900': 'hsl(202, 57%, 16%)',
            '950': 'hsl(202, 57%, 10%)',
            DEFAULT: '#235e80'
        },
        'neutral-50': '#181818',
        'neutral-100': '#ffffff',
        'neutral-200': '#f3f3f3',
        'neutral-300': '#919598',
        'neutral-400': '#000000',
        'neutral-500': '#232323',
        'neutral-600': '#d4d4d4',
        background: '#ffffff',
        foreground: '#000000'
    },
    fontFamily: {
        body: [
            'Suisseworks Webs',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '16.8px'
            }
        ],
        '14': [
            '14px',
            {
                lineHeight: '18.2px'
            }
        ],
        '16': [
            '16px',
            {
                lineHeight: 'normal'
            }
        ],
        '229.231': [
            '229.231px',
            {
                lineHeight: '229.231px'
            }
        ],
        '86.3077': [
            '86.3077px',
            {
                lineHeight: '77.6769px'
            }
        ],
        '53.2308': [
            '53.2308px',
            {
                lineHeight: '58.5538px'
            }
        ],
        '44.3077': [
            '44.3077px',
            {
                lineHeight: '44.3077px'
            }
        ],
        '28.6154': [
            '28.6154px',
            {
                lineHeight: '31.4769px'
            }
        ],
        '21.8462': [
            '21.8462px',
            {
                lineHeight: '26.2154px'
            }
        ],
        '17.8462': [
            '17.8462px',
            {
                lineHeight: '24.9846px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '18': '36px',
        '21': '42px',
        '29': '58px',
        '37': '74px',
        '43': '86px',
        '55': '110px',
        '98': '196px',
        '245': '490px',
        '63px': '63px',
        '115px': '115px',
        '131px': '131px',
        '177px': '177px',
        '457px': '457px',
        '473px': '473px'
    },
    borderRadius: {
        sm: '3px',
        md: '6px',
        full: '1280px'
    },
    screens: {
        md: '768px',
        lg: '1025px'
    },
    transitionDuration: {
        '1': '0.001s',
        '200': '0.2s',
        '300': '0.3s',
        '400': '0.4s'
    },
    transitionTimingFunction: {
        default: 'ease'
    },
    container: {
        center: true,
        padding: '0px'
    },
    maxWidth: {
        container: '2400px'
    }
},
  },
};
