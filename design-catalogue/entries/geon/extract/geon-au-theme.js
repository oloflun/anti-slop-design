// React Theme — extracted from https://geon.au/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '11': string;
    '12': string;
    '13': string;
    '15': string;
    '16': string;
    '18': string;
    '24': string;
    '33': string;
    '65': string;
 *   };
 *   space: {
    '4': string;
    '30': string;
    '40': string;
    '79': string;
    '108': string;
    '146': string;
    '225': string;
    '272': string;
    '308': string;
    '427': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
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
    "primary": "#f2eeea",
    "background": "#867c73",
    "foreground": "#000000",
    "neutral50": "#867c73",
    "neutral100": "#000000",
    "neutral200": "#34312e",
    "neutral300": "#6c645c",
    "neutral400": "#5e5853",
    "neutral500": "#474340",
    "neutral600": "#ffffff"
  },
  "fonts": {
    "body": "'GT Super Text', sans-serif"
  },
  "fontSizes": {
    "11": "11px",
    "12": "12px",
    "13": "13px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "24": "24px",
    "33": "33px",
    "65": "65px"
  },
  "space": {
    "4": "4px",
    "30": "30px",
    "40": "40px",
    "79": "79px",
    "108": "108px",
    "146": "146px",
    "225": "225px",
    "272": "272px",
    "308": "308px",
    "427": "427px"
  },
  "radii": {
    "xs": "1px",
    "sm": "5px",
    "md": "10px",
    "full": "1280px"
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
      "main": "#f2eeea",
      "light": "hsl(30, 24%, 95%)",
      "dark": "hsl(30, 24%, 78%)"
    },
    "background": {
      "default": "#867c73",
      "paper": "#353330"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#f2eeea"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "33px",
      "fontWeight": "500",
      "lineHeight": "33px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "500",
      "lineHeight": "normal"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    },
    "body2": {
      "fontSize": "15px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": []
};

export default theme;
