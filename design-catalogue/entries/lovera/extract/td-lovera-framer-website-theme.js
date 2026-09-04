// React Theme — extracted from https://td-lovera.framer.website
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
    '21': string;
    '24': string;
    '36': string;
    '48': string;
    '98': string;
    '100': string;
    '120': string;
    '152': string;
    '190': string;
    '320': string;
    '104.117': string;
    '64.855': string;
 *   };
 *   space: {
    '1': string;
    '80': string;
    '100': string;
    '120': string;
    '140': string;
    '150': string;
    '200': string;
 *   };
 *   radii: {
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
    "primary": "#ff531f",
    "secondary": "#0000ee",
    "accent": "#ff825c",
    "background": "#1e1f1f",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#171717",
    "neutral200": "#ffffff",
    "neutral300": "#767f7a",
    "neutral400": "#dddfde",
    "neutral500": "#f5f5f5",
    "neutral600": "#afb6b4",
    "neutral700": "#434645",
    "neutral800": "#fff0eb"
  },
  "fonts": {
    "body": "'Instrument Sans', sans-serif"
  },
  "fontSizes": {
    "21": "21px",
    "24": "24px",
    "36": "36px",
    "48": "48px",
    "98": "98px",
    "100": "100px",
    "120": "120px",
    "152": "152px",
    "190": "190px",
    "320": "320px",
    "104.117": "104.117px",
    "64.855": "64.855px"
  },
  "space": {
    "1": "1px",
    "80": "80px",
    "100": "100px",
    "120": "120px",
    "140": "140px",
    "150": "150px",
    "200": "200px"
  },
  "radii": {
    "md": "10px",
    "lg": "16px",
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
      "main": "#ff531f",
      "light": "hsl(14, 100%, 71%)",
      "dark": "hsl(14, 100%, 41%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#1e1f1f",
      "paper": "#f5f5f5"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "100px",
      "fontWeight": "500",
      "lineHeight": "95px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;
