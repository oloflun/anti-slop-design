// React Theme — extracted from https://areto.webflow.io/home-two
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
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '29': string;
    '30': string;
    '31': string;
    '40': string;
    '60': string;
    '128': string;
    '192': string;
    '102.4': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '30': string;
    '35': string;
    '38': string;
    '44': string;
    '48': string;
    '55': string;
    '60': string;
    '64': string;
    '67': string;
    '70': string;
    '80': string;
    '90': string;
    '100': string;
    '108': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    lg: string;
    xl: string;
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
    "primary": "#f8fa8d",
    "secondary": "#36503f",
    "accent": "#120a0e",
    "background": "#f5f5f5",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#4d4d4d",
    "neutral200": "#ece7e4",
    "neutral300": "#ffffff",
    "neutral400": "#cccccc",
    "neutral500": "#333333",
    "neutral600": "#f5f5f5",
    "neutral700": "#26382c",
    "neutral800": "#dddddd"
  },
  "fonts": {
    "body": "'Inter Tight', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "29": "29px",
    "30": "30px",
    "31": "31px",
    "40": "40px",
    "60": "60px",
    "128": "128px",
    "192": "192px",
    "102.4": "102.4px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "30": "30px",
    "35": "35px",
    "38": "38px",
    "44": "44px",
    "48": "48px",
    "55": "55px",
    "60": "60px",
    "64": "64px",
    "67": "67px",
    "70": "70px",
    "80": "80px",
    "90": "90px",
    "100": "100px",
    "108": "108px"
  },
  "radii": {
    "md": "8px",
    "lg": "11px",
    "xl": "18px",
    "full": "999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0.449482px",
    "lg": "rgba(0, 0, 0, 0.35) 0px 4px 14px 0px",
    "xl": "rgba(0, 0, 0, 0.65) 0px 18px 40px -18px"
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
      "main": "#f8fa8d",
      "light": "hsl(61, 92%, 92%)",
      "dark": "hsl(61, 92%, 62%)"
    },
    "secondary": {
      "main": "#36503f",
      "light": "hsl(141, 19%, 41%)",
      "dark": "hsl(141, 19%, 11%)"
    },
    "background": {
      "default": "#f5f5f5",
      "paper": "#f8fa8d"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#4d4d4d"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "40px",
      "fontWeight": "500",
      "lineHeight": "40px"
    },
    "h2": {
      "fontSize": "31px",
      "fontWeight": "400",
      "lineHeight": "31px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0.449482px",
    "rgba(0, 0, 0, 0.35) 0px 4px 14px 0px",
    "rgba(0, 0, 0, 0.55) 0px 12px 26px -18px",
    "rgba(0, 0, 0, 0.65) 0px 18px 40px -18px"
  ]
};

export default theme;
