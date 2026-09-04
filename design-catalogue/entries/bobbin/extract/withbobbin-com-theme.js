// React Theme — extracted from https://withbobbin.com/
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
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '20': string;
    '24': string;
    '32': string;
    '34': string;
    '48': string;
    '60': string;
 *   };
 *   space: {
    '1': string;
    '51': string;
    '56': string;
    '74': string;
    '80': string;
    '89': string;
    '107': string;
    '120': string;
    '137': string;
    '150': string;
    '160': string;
    '200': string;
    '285': string;
    '290': string;
    '330': string;
    '343': string;
 *   };
 *   radii: {
    sm: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
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
    "primary": "#fbf27e",
    "secondary": "#f7f4f0",
    "accent": "#faf39b",
    "background": "#000000",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#70685c",
    "neutral300": "#544e45",
    "neutral400": "#8c8273",
    "neutral500": "#a39b8f",
    "neutral600": "#cdc6bc",
    "neutral700": "#2a241d",
    "neutral800": "#413c33",
    "neutral900": "#e8e4de"
  },
  "fonts": {
    "body": "'GT Alpina', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "32": "32px",
    "34": "34px",
    "48": "48px",
    "60": "60px"
  },
  "space": {
    "1": "1px",
    "51": "51px",
    "56": "56px",
    "74": "74px",
    "80": "80px",
    "89": "89px",
    "107": "107px",
    "120": "120px",
    "137": "137px",
    "150": "150px",
    "160": "160px",
    "200": "200px",
    "285": "285px",
    "290": "290px",
    "330": "330px",
    "343": "343px"
  },
  "radii": {
    "sm": "5px",
    "lg": "14px",
    "xl": "24px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px",
    "lg": "rgba(250, 177, 47, 0.15) 0px 7px 15px 0px, rgba(250, 177, 47, 0.13) 0px 27px 27px 0px, rgba(250, 177, 47, 0.08) 0px 61px 37px 0px"
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
      "main": "#fbf27e",
      "light": "hsl(56, 94%, 89%)",
      "dark": "hsl(56, 94%, 59%)"
    },
    "secondary": {
      "main": "#f7f4f0",
      "light": "hsl(34, 30%, 95%)",
      "dark": "hsl(34, 30%, 80%)"
    },
    "background": {
      "default": "#000000",
      "paper": "#2a241d"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "32px",
      "fontWeight": "500",
      "lineHeight": "35.2px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "36px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "26px"
    }
  },
  "shape": {
    "borderRadius": 5
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px",
    "rgba(250, 177, 47, 0.15) 0px 7px 15px 0px, rgba(250, 177, 47, 0.13) 0px 27px 27px 0px, rgba(250, 177, 47, 0.08) 0px 61px 37px 0px"
  ]
};

export default theme;
