// React Theme — extracted from https://nura-ai.framer.website/
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
    '16': string;
    '18': string;
    '20': string;
    '22': string;
    '26': string;
    '28': string;
    '36': string;
    '48': string;
    '90': string;
    '100': string;
    '120': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '28': string;
    '32': string;
    '40': string;
    '64': string;
    '80': string;
    '100': string;
    '120': string;
    '300': string;
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
    xs: string;
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
    "primary": "#0000ee",
    "secondary": "#ff5f54",
    "accent": "#ffbe32",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#1a1a1a",
    "neutral300": "#5d5d5d",
    "neutral400": "#464646",
    "neutral500": "#737373",
    "neutral600": "#242424",
    "neutral700": "#2e2e2e",
    "neutral800": "#ededed",
    "neutral900": "#8c8c8c"
  },
  "fonts": {
    "body": "'Instrument Serif', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "22": "22px",
    "26": "26px",
    "28": "28px",
    "36": "36px",
    "48": "48px",
    "90": "90px",
    "100": "100px",
    "120": "120px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "40": "40px",
    "64": "64px",
    "80": "80px",
    "100": "100px",
    "120": "120px",
    "300": "300px"
  },
  "radii": {
    "xs": "1px",
    "sm": "4px",
    "md": "8px",
    "lg": "15px",
    "xl": "24px",
    "full": "100px"
  },
  "shadows": {
    "sm": "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "xs": "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
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
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "secondary": {
      "main": "#ff5f54",
      "light": "hsl(4, 100%, 81%)",
      "dark": "hsl(4, 100%, 51%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#f8f8f8"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "36px",
      "fontWeight": "500",
      "lineHeight": "39.6px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "500",
      "lineHeight": "33.6px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgb(255, 255, 255) 0px 0px 0px 2px",
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;
