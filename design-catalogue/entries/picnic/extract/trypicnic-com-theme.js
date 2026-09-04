// React Theme — extracted from https://trypicnic.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '30': string;
    '36': string;
    '60': string;
    '82': string;
 *   };
 *   space: {
    '1': string;
    '30': string;
    '40': string;
    '48': string;
    '56': string;
    '70': string;
    '100': string;
    '120': string;
    '160': string;
    '182': string;
    '190': string;
    '195': string;
    '240': string;
    '282': string;
    '320': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    lg: string;
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
    "primary": "#f7f6f2",
    "secondary": "#f74c25",
    "background": "#f7f6f2",
    "foreground": "#f74c25",
    "neutral50": "#e5e7eb",
    "neutral100": "#000000",
    "neutral200": "#12110c",
    "neutral300": "#525252",
    "neutral400": "#ffffff",
    "neutral500": "#cacac3"
  },
  "fonts": {
    "body": "'__interDisplay_4fc95a', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "30": "30px",
    "36": "36px",
    "60": "60px",
    "82": "82px"
  },
  "space": {
    "1": "1px",
    "30": "30px",
    "40": "40px",
    "48": "48px",
    "56": "56px",
    "70": "70px",
    "100": "100px",
    "120": "120px",
    "160": "160px",
    "182": "182px",
    "190": "190px",
    "195": "195px",
    "240": "240px",
    "282": "282px",
    "320": "320px"
  },
  "radii": {
    "md": "8px",
    "lg": "16px",
    "full": "9999px"
  },
  "shadows": {
    "lg": "rgba(0, 0, 0, 0.26) 0px 4px 25px 0px"
  },
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
      "main": "#f7f6f2",
      "light": "hsl(48, 24%, 95%)",
      "dark": "hsl(48, 24%, 81%)"
    },
    "secondary": {
      "main": "#f74c25",
      "light": "hsl(11, 93%, 71%)",
      "dark": "hsl(11, 93%, 41%)"
    },
    "background": {
      "default": "#f7f6f2",
      "paper": "#f74c25"
    },
    "text": {
      "primary": "#f74c25",
      "secondary": "#f7f6f2"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "500",
      "lineHeight": "39.6px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "500",
      "lineHeight": "28.8px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "500",
      "lineHeight": "22px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0.26) 0px 4px 25px 0px"
  ]
};

export default theme;
