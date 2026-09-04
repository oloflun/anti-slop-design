// React Theme — extracted from https://futurefur.com.au/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '11': string;
    '12': string;
    '13': string;
    '14': string;
    '15': string;
    '16': string;
    '20': string;
    '32': string;
    '40': string;
    '44': string;
    '55': string;
    '13.3333': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '30': string;
    '35': string;
    '40': string;
    '44': string;
    '48': string;
    '56': string;
    '60': string;
    '70': string;
    '80': string;
    '110': string;
    '128': string;
    '256': string;
    '385': string;
    '425': string;
 *   };
 *   radii: {
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
    "primary": "#00a000",
    "secondary": "#d32c00",
    "accent": "#ebd2c2",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#f6f6f6",
    "neutral300": "#242323"
  },
  "fonts": {
    "body": "'GTStandard-M', sans-serif"
  },
  "fontSizes": {
    "11": "11px",
    "12": "12px",
    "13": "13px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "20": "20px",
    "32": "32px",
    "40": "40px",
    "44": "44px",
    "55": "55px",
    "13.3333": "13.3333px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "30": "30px",
    "35": "35px",
    "40": "40px",
    "44": "44px",
    "48": "48px",
    "56": "56px",
    "60": "60px",
    "70": "70px",
    "80": "80px",
    "110": "110px",
    "128": "128px",
    "256": "256px",
    "385": "385px",
    "425": "425px"
  },
  "radii": {
    "full": "50px"
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
      "main": "#00a000",
      "light": "hsl(120, 100%, 46%)",
      "dark": "hsl(120, 100%, 16%)"
    },
    "secondary": {
      "main": "#d32c00",
      "light": "hsl(13, 100%, 56%)",
      "dark": "hsl(13, 100%, 26%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#d32c00"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#d32c00"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "700",
      "lineHeight": "36px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "700",
      "lineHeight": "24px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "700",
      "lineHeight": "20px"
    }
  },
  "shape": {
    "borderRadius": 40
  },
  "shadows": []
};

export default theme;
