// React Theme — extracted from https://dope.security
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
    mono: string;
 *   };
 *   fontSizes: {
    '14': string;
    '16': string;
    '20': string;
    '24': string;
    '28': string;
    '32': string;
    '40': string;
    '48': string;
    '64': string;
    '80': string;
    '88': string;
    '18.4': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '32': string;
    '38': string;
    '45': string;
    '64': string;
    '72': string;
    '80': string;
    '96': string;
    '128': string;
    '136': string;
    '160': string;
    '208': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    xs: string;
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
    "primary": "#edc3c4",
    "secondary": "#f7f9fa",
    "accent": "#af50ff",
    "background": "#090909",
    "foreground": "#000000",
    "neutral50": "#f0f0f0",
    "neutral100": "#000000",
    "neutral200": "#090909",
    "neutral300": "#333333",
    "neutral400": "#475467",
    "neutral500": "#344054",
    "neutral600": "#dae0e8",
    "neutral700": "#d0d5dd",
    "neutral800": "#878787"
  },
  "fonts": {
    "body": "'Karla', sans-serif",
    "mono": "'Whyte Inktrap Mono', monospace"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "64": "64px",
    "80": "80px",
    "88": "88px",
    "18.4": "18.4px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "32": "32px",
    "38": "38px",
    "45": "45px",
    "64": "64px",
    "72": "72px",
    "80": "80px",
    "96": "96px",
    "128": "128px",
    "136": "136px",
    "160": "160px",
    "208": "208px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "11px",
    "xl": "24px",
    "full": "1584px"
  },
  "shadows": {
    "xs": "rgba(16, 24, 40, 0.05) 0px 1px 2px 0px",
    "sm": "rgba(0, 0, 0, 0.25) 0px 3.2px 3.2px 0px",
    "lg": "rgba(0, 0, 0, 0.08) 0px 12px 16px -4px, rgba(16, 24, 40, 0.03) 0px 4px 6px -2px"
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
      "main": "#edc3c4",
      "light": "hsl(359, 54%, 95%)",
      "dark": "hsl(359, 54%, 70%)"
    },
    "secondary": {
      "main": "#f7f9fa",
      "light": "hsl(200, 23%, 95%)",
      "dark": "hsl(200, 23%, 82%)"
    },
    "background": {
      "default": "#090909",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#333333"
    }
  },
  "typography": {
    "fontFamily": "'GrandSlang', sans-serif",
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
    "rgb(175, 80, 255) -0.5px -0.5px 0px 0px inset, rgb(175, 80, 255) -1px 2px 0px -2px inset, rgb(175, 80, 255) -1px 0px 0px -0.1px inset",
    "rgba(16, 24, 40, 0.06) 0px 1px 1px 0px, rgba(16, 24, 40, 0.1) 0px 1px 2px 0px",
    "rgba(16, 24, 40, 0.05) 0px 1px 2px 0px",
    "rgba(0, 0, 0, 0.25) 0px 3.2px 3.2px 0px",
    "rgba(102, 126, 234, 0.3) 0px 4px 20px 0px"
  ]
};

export default theme;
