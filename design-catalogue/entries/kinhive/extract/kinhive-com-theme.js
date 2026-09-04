// React Theme — extracted from https://kinhive.com
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
    '14': string;
    '15': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '32': string;
    '40': string;
    '44': string;
    '48': string;
    '72': string;
    '96': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '30': string;
    '39': string;
    '48': string;
    '63': string;
    '69': string;
    '80': string;
    '120': string;
    '144': string;
    '187': string;
    '245': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
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
    "primary": "#f8f9b8",
    "secondary": "#f7f7f5",
    "accent": "#fd8143",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#22201f",
    "neutral200": "#777777",
    "neutral300": "#ffffff",
    "neutral400": "#646464",
    "neutral500": "#d8d7d3",
    "neutral600": "#0f0e0e",
    "neutral700": "#eeedeb",
    "neutral800": "#e0e0e0",
    "neutral900": "#555555"
  },
  "fonts": {
    "body": "'Affairs', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "32": "32px",
    "40": "40px",
    "44": "44px",
    "48": "48px",
    "72": "72px",
    "96": "96px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "30": "30px",
    "39": "39px",
    "48": "48px",
    "63": "63px",
    "69": "69px",
    "80": "80px",
    "120": "120px",
    "144": "144px",
    "187": "187px",
    "245": "245px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "full": "900px"
  },
  "shadows": {
    "xl": "rgba(0, 0, 0, 0.15) 0px 8px 32px 0px"
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
      "main": "#f8f9b8",
      "light": "hsl(61, 84%, 95%)",
      "dark": "hsl(61, 84%, 70%)"
    },
    "secondary": {
      "main": "#f7f7f5",
      "light": "hsl(60, 11%, 95%)",
      "dark": "hsl(60, 11%, 81%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#f8f9b8"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'Helvetica', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "38.4px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0.15) 0px 8px 32px 0px"
  ]
};

export default theme;
