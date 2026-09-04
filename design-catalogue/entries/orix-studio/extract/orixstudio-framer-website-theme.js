// React Theme — extracted from https://orixstudio.framer.website/
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
    '28': string;
    '32': string;
    '42': string;
    '180': string;
    '178.579': string;
 *   };
 *   space: {
    '1': string;
    '20': string;
    '32': string;
    '54': string;
    '64': string;
    '80': string;
    '100': string;
    '130': string;
    '200': string;
 *   };
 *   radii: {
    md: string;
    lg: string;
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
    "primary": "#df0203",
    "secondary": "#0000ee",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#646464",
    "neutral300": "#767676",
    "neutral400": "#3d3d3d",
    "neutral500": "#d6d6d6"
  },
  "fonts": {
    "body": "'Open Sauce One', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "42": "42px",
    "180": "180px",
    "178.579": "178.579px"
  },
  "space": {
    "1": "1px",
    "20": "20px",
    "32": "32px",
    "54": "54px",
    "64": "64px",
    "80": "80px",
    "100": "100px",
    "130": "130px",
    "200": "200px"
  },
  "radii": {
    "md": "10px",
    "lg": "16px",
    "full": "999px"
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
      "main": "#df0203",
      "light": "hsl(360, 98%, 59%)",
      "dark": "hsl(360, 98%, 29%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Instrument Sans', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "500",
      "lineHeight": "44.8px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "500",
      "lineHeight": "33.6px"
    }
  },
  "shape": {
    "borderRadius": 10
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.14) 0px 0.711334px 0.711334px -0.55px, rgba(0, 0, 0, 0.14) 0px 1.93715px 1.93715px -1.1px, rgba(0, 0, 0, 0.13) 0px 4.25328px 4.25328px -1.65px, rgba(0, 0, 0, 0.13) 0px 9.44132px 9.44132px -2.2px, rgba(0, 0, 0, 0.11) 0px 24px 24px -2.75px",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  ]
};

export default theme;
