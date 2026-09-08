/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
    colors: {
        primary: {
            '50': 'hsl(222, 47%, 97%)',
            '100': 'hsl(222, 47%, 94%)',
            '200': 'hsl(222, 47%, 86%)',
            '300': 'hsl(222, 47%, 76%)',
            '400': 'hsl(222, 47%, 64%)',
            '500': 'hsl(222, 47%, 50%)',
            '600': 'hsl(222, 47%, 40%)',
            '700': 'hsl(222, 47%, 32%)',
            '800': 'hsl(222, 47%, 24%)',
            '900': 'hsl(222, 47%, 16%)',
            '950': 'hsl(222, 47%, 10%)',
            DEFAULT: '#0f172a'
        },
        secondary: {
            '50': 'hsl(161, 94%, 97%)',
            '100': 'hsl(161, 94%, 94%)',
            '200': 'hsl(161, 94%, 86%)',
            '300': 'hsl(161, 94%, 76%)',
            '400': 'hsl(161, 94%, 64%)',
            '500': 'hsl(161, 94%, 50%)',
            '600': 'hsl(161, 94%, 40%)',
            '700': 'hsl(161, 94%, 32%)',
            '800': 'hsl(161, 94%, 24%)',
            '900': 'hsl(161, 94%, 16%)',
            '950': 'hsl(161, 94%, 10%)',
            DEFAULT: '#059669'
        },
        accent: {
            '50': 'hsl(239, 84%, 97%)',
            '100': 'hsl(239, 84%, 94%)',
            '200': 'hsl(239, 84%, 86%)',
            '300': 'hsl(239, 84%, 76%)',
            '400': 'hsl(239, 84%, 64%)',
            '500': 'hsl(239, 84%, 50%)',
            '600': 'hsl(239, 84%, 40%)',
            '700': 'hsl(239, 84%, 32%)',
            '800': 'hsl(239, 84%, 24%)',
            '900': 'hsl(239, 84%, 16%)',
            '950': 'hsl(239, 84%, 10%)',
            DEFAULT: '#6366f1'
        },
        'neutral-50': '#e5e7eb',
        'neutral-100': '#ffffff',
        'neutral-200': '#475569',
        'neutral-300': '#64748b',
        'neutral-400': '#94a3b8',
        'neutral-500': '#eef2ff',
        'neutral-600': '#334155',
        'neutral-700': '#ecfdf5',
        background: '#fbfaf7',
        foreground: '#1f2937'
    },
    fontFamily: {
        sans: [
            'Inter',
            'sans-serif'
        ]
    },
    fontSize: {
        '12': [
            '12px',
            {
                lineHeight: '16px'
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
                lineHeight: '24px'
            }
        ],
        '18': [
            '18px',
            {
                lineHeight: '29.25px'
            }
        ],
        '20': [
            '20px',
            {
                lineHeight: '28px'
            }
        ],
        '30': [
            '30px',
            {
                lineHeight: '36px'
            }
        ],
        '36': [
            '36px',
            {
                lineHeight: '40px'
            }
        ],
        '48': [
            '48px',
            {
                lineHeight: '48px'
            }
        ],
        '60': [
            '60px',
            {
                lineHeight: '60px',
                letterSpacing: '-1.5px'
            }
        ]
    },
    spacing: {
        '1': '2px',
        '20': '40px',
        '24': '48px',
        '32': '64px',
        '40': '80px',
        '48': '96px',
        '64': '128px',
        '108': '216px',
        '132': '264px'
    },
    borderRadius: {
        md: '8px',
        lg: '16px',
        full: '9999px'
    },
    boxShadow: {
        sm: 'rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px'
    },
    screens: {
        md: '768px'
    },
    container: {
        center: true,
        padding: '24px'
    },
    maxWidth: {
        container: '1152px'
    }
},
  },
};
