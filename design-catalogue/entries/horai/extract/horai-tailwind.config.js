/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(359, 100%, 97%)',
            '100': 'hsl(359, 100%, 94%)',
            '200': 'hsl(359, 100%, 86%)',
            '300': 'hsl(359, 100%, 76%)',
            '400': 'hsl(359, 100%, 64%)',
            '500': 'hsl(359, 100%, 50%)',
            '600': 'hsl(359, 100%, 40%)',
            '700': 'hsl(359, 100%, 32%)',
            '800': 'hsl(359, 100%, 24%)',
            '900': 'hsl(359, 100%, 16%)',
            '950': 'hsl(359, 100%, 10%)',
            DEFAULT: '#650001'
        },
        secondary: {
            '50': 'hsl(148, 61%, 97%)',
            '100': 'hsl(148, 61%, 94%)',
            '200': 'hsl(148, 61%, 86%)',
            '300': 'hsl(148, 61%, 76%)',
            '400': 'hsl(148, 61%, 64%)',
            '500': 'hsl(148, 61%, 50%)',
            '600': 'hsl(148, 61%, 40%)',
            '700': 'hsl(148, 61%, 32%)',
            '800': 'hsl(148, 61%, 24%)',
            '900': 'hsl(148, 61%, 16%)',
            '950': 'hsl(148, 61%, 10%)',
            DEFAULT: '#06190f'
        },
        accent: {
            '50': 'hsl(36, 46%, 97%)',
            '100': 'hsl(36, 46%, 94%)',
            '200': 'hsl(36, 46%, 86%)',
            '300': 'hsl(36, 46%, 76%)',
            '400': 'hsl(36, 46%, 64%)',
            '500': 'hsl(36, 46%, 50%)',
            '600': 'hsl(36, 46%, 40%)',
            '700': 'hsl(36, 46%, 32%)',
            '800': 'hsl(36, 46%, 24%)',
            '900': 'hsl(36, 46%, 16%)',
            '950': 'hsl(36, 46%, 10%)',
            DEFAULT: '#e0cbab'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#040202',
        'neutral-200': '#1e1513',
        background: '#e0cbab',
        foreground: '#040202'
    },
    fontFamily: {
        body: [
            'Noto Serif JP',
            'sans-serif'
        ],
        heading: [
            'Cinzel',
            'sans-serif'
        ]
    },
    fontSize: {
        '114': [
            '114px',
            {
                lineHeight: '114px',
                letterSpacing: '4.56px'
            }
        ],
        '192': [
            '192px',
            {
                lineHeight: '172.8px',
                letterSpacing: '11.52px'
            }
        ],
        '89.6': [
            '89.6px',
            {
                lineHeight: '80.64px',
                letterSpacing: '3.584px'
            }
        ],
        '81.92': [
            '81.92px',
            {
                lineHeight: '77.824px',
                letterSpacing: '4.9152px'
            }
        ],
        '71.68': [
            '71.68px',
            {
                lineHeight: '71.68px',
                letterSpacing: '4.3008px'
            }
        ],
        '58.88': [
            '58.88px',
            {
                lineHeight: '58.88px',
                letterSpacing: '1.7664px'
            }
        ],
        '51.2': [
            '51.2px',
            {
                lineHeight: '51.2px'
            }
        ],
        '46.08': [
            '46.08px',
            {
                lineHeight: '46.08px',
                letterSpacing: '2.7648px'
            }
        ],
        '35.84': [
            '35.84px',
            {
                lineHeight: '45.8752px',
                letterSpacing: '12.9024px'
            }
        ],
        '34.2': [
            '34.2px',
            {
                lineHeight: '34.2px'
            }
        ],
        '28.5': [
            '28.5px',
            {
                lineHeight: '38px',
                letterSpacing: '5.13px'
            }
        ],
        '28.16': [
            '28.16px',
            {
                lineHeight: '38.72px',
                letterSpacing: '3.9424px'
            }
        ],
        '26.6': [
            '26.6px',
            {
                lineHeight: '41.23px'
            }
        ],
        '25.6': [
            '25.6px',
            {
                lineHeight: '25.6px',
                letterSpacing: '6.656px'
            }
        ],
        '24.7': [
            '24.7px',
            {
                lineHeight: '39.52px'
            }
        ]
    },
    spacing: {
        '5': '10px',
        '57': '114px',
        '76': '152px',
        '95': '190px',
        '205': '410px',
        '57px': '57px',
        '67px': '67px',
        '209px': '209px'
    },
    screens: {
        md: '768px',
        lg: '1024px'
    },
    transitionDuration: {
        '120': '0.12s',
        '150': '0.15s',
        '300': '0.3s',
        '500': '0.5s',
        '900': '0.9s',
        '1300': '1.3s',
        '1400': '1.4s'
    },
    transitionTimingFunction: {
        custom: 'cubic-bezier(0.16, 1, 0.3, 1)',
        default: 'ease'
    },
    container: {
        center: true,
        padding: '66.5px'
    },
    maxWidth: {
        container: '1880px'
    }
},
  },
};
