// React Theme — extracted from https://drinkolipop.com
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
    '16': string;
    '18': string;
    '20': string;
    '22': string;
    '24': string;
    '32': string;
    '40': string;
    '48': string;
    '50': string;
    '52': string;
    '54': string;
    '80': string;
 *   };
 *   space: {
    '0': string;
    '30': string;
    '36': string;
    '40': string;
    '45': string;
    '48': string;
    '53': string;
    '60': string;
    '63': string;
    '72': string;
    '80': string;
    '86': string;
    '92': string;
    '106': string;
    '120': string;
    '160': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    md: string;
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
    "primary": "#034638",
    "secondary": "#ffff7d",
    "accent": "#98e1c3",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#3a3a3a",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#fff6ea",
    "neutral400": "#9a9a9a",
    "neutral500": "#737373",
    "neutral600": "#4f7456",
    "neutral700": "#cccccc",
    "neutral800": "#e3e3e3",
    "neutral900": "#f0f0f0"
  },
  "fonts": {
    "body": "'SF-Secondary-Font', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "22": "22px",
    "24": "24px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "50": "50px",
    "52": "52px",
    "54": "54px",
    "80": "80px"
  },
  "space": {
    "0": "0px",
    "30": "30px",
    "36": "36px",
    "40": "40px",
    "45": "45px",
    "48": "48px",
    "53": "53px",
    "60": "60px",
    "63": "63px",
    "72": "72px",
    "80": "80px",
    "86": "86px",
    "92": "92px",
    "106": "106px",
    "120": "120px",
    "160": "160px"
  },
  "radii": {
    "xs": "2px",
    "sm": "5px",
    "md": "8px",
    "lg": "16px",
    "xl": "24px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgb(20, 67, 61) 0px 0px 0px 1.5px",
    "md": "rgba(0, 0, 0, 0.25) 0px 4px 8px 0px",
    "xl": "rgba(0, 0, 0, 0.12) 0px 0px 80px 0px"
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
      "main": "#034638",
      "light": "hsl(167, 92%, 29%)",
      "dark": "hsl(167, 92%, 10%)"
    },
    "secondary": {
      "main": "#ffff7d",
      "light": "hsl(60, 100%, 90%)",
      "dark": "hsl(60, 100%, 60%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#14433d"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "900",
      "lineHeight": "44px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
    "rgb(3, 70, 56) 0px 0px 0px 1.5px",
    "rgb(20, 67, 61) 0px 0px 0px 1.5px",
    "rgba(0, 0, 0, 0.25) 0px 4px 8px 0px",
    "rgba(0, 0, 0, 0.07) 8px 0px 32px 0px"
  ]
};

export default theme;
