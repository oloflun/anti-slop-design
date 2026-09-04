// React Theme — extracted from https://snapifye.webflow.io/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '20': string;
    '24': string;
    '60': string;
    '184': string;
    '158.113': string;
    '133.334': string;
    '113.208': string;
    '66.792': string;
    '47.5462': string;
    '46.5875': string;
    '23.4336': string;
    '23.2458': string;
 *   };
 *   space: {
    '1': string;
    '40': string;
    '60': string;
    '80': string;
    '100': string;
    '115': string;
    '120': string;
    '140': string;
    '175': string;
    '180': string;
    '203': string;
    '265': string;
    '420': string;
    '440': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#f9dcc5",
    "secondary": "#701e1f",
    "accent": "#ff2f2f",
    "background": "#f9dcc5",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#000000",
    "neutral200": "#161616",
    "neutral300": "#474747",
    "neutral400": "#222222"
  },
  "fonts": {
    "body": "'PT Sans', sans-serif"
  },
  "fontSizes": {
    "20": "20px",
    "24": "24px",
    "60": "60px",
    "184": "184px",
    "158.113": "158.113px",
    "133.334": "133.334px",
    "113.208": "113.208px",
    "66.792": "66.792px",
    "47.5462": "47.5462px",
    "46.5875": "46.5875px",
    "23.4336": "23.4336px",
    "23.2458": "23.2458px"
  },
  "space": {
    "1": "1px",
    "40": "40px",
    "60": "60px",
    "80": "80px",
    "100": "100px",
    "115": "115px",
    "120": "120px",
    "140": "140px",
    "175": "175px",
    "180": "180px",
    "203": "203px",
    "265": "265px",
    "420": "420px",
    "440": "440px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "16px",
    "xl": "24px",
    "full": "99px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#f9dcc5",
      "light": "hsl(27, 81%, 95%)",
      "dark": "hsl(27, 81%, 72%)"
    },
    "secondary": {
      "main": "#701e1f",
      "light": "hsl(359, 58%, 43%)",
      "dark": "hsl(359, 58%, 13%)"
    },
    "background": {
      "default": "#f9dcc5",
      "paper": "#701e1f"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#701e1f"
    }
  },
  "typography": {
    "fontFamily": "'Librecaslontext', sans-serif",
    "h1": {
      "fontSize": "60px",
      "fontWeight": "700",
      "lineHeight": "60px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;
